"""Read-only RF executable inventory. No target execution or network access."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import struct
import sys


MACHINES = {0x014C: "x86", 0x8664: "x64", 0xAA64: "arm64"}


def is_link_or_junction(path):
    info = path.lstat()
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0) & 0x400
    )


def inspect_binary(path):
    """Hash one binary and inspect a bounded PE header without loading code."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        before = os.fstat(stream.fileno())
        header = stream.read(64)
        architecture = "not_pe"
        if len(header) == 64 and header[:2] == b"MZ":
            offset = struct.unpack_from("<I", header, 60)[0]
            architecture = "invalid_pe"
            if 64 <= offset <= before.st_size - 24:
                stream.seek(offset)
                pe = stream.read(24)
                if len(pe) == 24 and pe[:4] == b"PE\0\0":
                    machine = struct.unpack_from("<H", pe, 4)[0]
                    architecture = MACHINES.get(machine, "unknown_0x%04x" % machine)
        stream.seek(0)
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
        after = os.fstat(stream.fileno())
        if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
            raise OSError("File changed during inventory; retry with stable test copies")
    return {"size_bytes": after.st_size, "sha256": digest.hexdigest(),
            "pe_architecture": architecture}


def inventory(root, label):
    root = Path(root)
    if is_link_or_junction(root):
        raise ValueError("Root must be a real directory, not a link or junction")
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Root must be a directory")
    report = {"schema_version": 1, "label": label,
              "rf_version": "unverified", "files": [], "errors": [],
              "skipped_links": 0}

    def record_walk_error(error):
        report["errors"].append({"path": "<directory scan>",
                                 "error_type": type(error).__name__})

    for directory, dirs, files in os.walk(root, followlinks=False, onerror=record_walk_error):
        kept = []
        for name in sorted(dirs):
            path = Path(directory) / name
            try:
                if is_link_or_junction(path):
                    report["skipped_links"] += 1
                else:
                    kept.append(name)
            except OSError as error:
                report["errors"].append({"path": path.relative_to(root).as_posix(),
                                         "error_type": type(error).__name__})
        dirs[:] = kept
        for name in sorted(files):
            path = Path(directory) / name
            if path.suffix.lower() not in {".exe", ".dll"}:
                continue
            relative = path.relative_to(root).as_posix()
            try:
                if is_link_or_junction(path):
                    report["skipped_links"] += 1
                    continue
                if not path.is_file():
                    continue
                entry = inspect_binary(path)
                report["files"].append({"path": relative, **entry})
            except OSError as error:
                report["errors"].append({"path": relative,
                                         "error_type": type(error).__name__})
    report["files"].sort(key=lambda entry: entry["path"])
    report["complete"] = not report["errors"]
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--label", required=True, choices=["client", "server"])
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve(strict=True)
        output = args.output.absolute()
        # Keep outputs out of the game directory and avoid overwriting any file.
        if root == output or root in output.resolve().parents:
            raise ValueError("Output must be outside the RF root directory")
        report = inventory(args.root, args.label)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("x", encoding="utf-8") as stream:
            json.dump(report, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
    except (OSError, ValueError) as error:
        print("Inventory failed (%s): %s" % (type(error).__name__, error), file=sys.stderr)
        return 2
    print("Inventory saved: %d binaries, %d errors. No files uploaded." % (
        len(report["files"]), len(report["errors"])))
    return 0 if report["complete"] else 2


if __name__ == "__main__":
    sys.exit(main())
