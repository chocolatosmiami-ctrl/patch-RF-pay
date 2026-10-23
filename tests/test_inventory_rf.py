import hashlib
import importlib.util
from pathlib import Path
import struct
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    "inventory_rf", Path(__file__).resolve().parents[1] / "tools" / "inventory_rf.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def pe_bytes(machine):
    data = bytearray(88)
    data[:2] = b"MZ"
    struct.pack_into("<I", data, 60, 64)
    data[64:68] = b"PE\0\0"
    struct.pack_into("<H", data, 68, machine)
    return bytes(data)


class InventoryTests(unittest.TestCase):
    def test_hash_architectures_and_no_secret_configuration(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name, machine in [("client.exe", 0x14C), ("server.DLL", 0x8664)]:
                (root / name).write_bytes(pe_bytes(machine))
            (root / "Main.ini").write_text("password=DO_NOT_READ")
            report = MODULE.inventory(root, "client")
            self.assertTrue(report["complete"])
            self.assertEqual(len(report["files"]), 2)
            first, second = report["files"]
            self.assertEqual(first["pe_architecture"], "x86")
            self.assertEqual(second["pe_architecture"], "x64")
            self.assertEqual(first["sha256"], hashlib.sha256(pe_bytes(0x14C)).hexdigest())
            self.assertNotIn("DO_NOT_READ", str(report))
            self.assertEqual(report["rf_version"], "unverified")

    def test_truncated_and_unbounded_offsets_are_not_accepted(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "broken.exe"
            path.write_bytes(b"MZ")
            self.assertEqual(MODULE.inspect_binary(path)["pe_architecture"], "not_pe")
            data = bytearray(64)
            data[:2] = b"MZ"
            struct.pack_into("<I", data, 60, 0xFFFFFFFF)
            path.write_bytes(data)
            self.assertEqual(MODULE.inspect_binary(path)["pe_architecture"], "invalid_pe")

    def test_output_cannot_modify_game_directory_or_overwrite_report(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "rf"
            root.mkdir()
            (root / "client.exe").write_bytes(pe_bytes(0x14C))
            inside = root / "report.json"
            self.assertEqual(MODULE.main(["--root", str(root), "--label", "client",
                                          "--output", str(inside)]), 2)
            self.assertFalse(inside.exists())
            output = Path(folder) / "report.json"
            args = ["--root", str(root), "--label", "client", "--output", str(output)]
            self.assertEqual(MODULE.main(args), 0)
            original = output.read_bytes()
            self.assertEqual(MODULE.main(args), 2)
            self.assertEqual(output.read_bytes(), original)

    def test_symlink_target_is_not_scanned(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "rf"
            root.mkdir()
            outside = Path(folder) / "outside"
            outside.mkdir()
            (outside / "secret.exe").write_bytes(pe_bytes(0x14C))
            try:
                (root / "linked").symlink_to(outside, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("Symlink creation unavailable")
            report = MODULE.inventory(root, "server")
            self.assertEqual(report["files"], [])
            self.assertEqual(report["skipped_links"], 1)


if __name__ == "__main__":
    unittest.main()
