# Analisis awal executable RF

Tanggal: 24 Oktober 2026. Target adalah dua blob pada commit `d67e0b6e47e87c67403118bc292a38d45a85ffc0`.

## Metode dan batas pemeriksaan

File diambil dari repository dan diperiksa dengan `file`, `sha256sum`, GNU `objdump`, serta pembacaan header PE/import descriptor dan pencarian string statis menggunakan Python. Tidak ada executable target yang dijalankan, diubah, di-unpack atau dihubungkan ke database/network. MCP REA laptop tidak tersedia di sesi analisis ini; laporan ini tidak mengklaim menggunakan REA.

Hasil ini adalah identifikasi awal, bukan dekompilasi penuh atau bukti kompatibilitas gameplay. Timestamp dan string build tidak membuktikan versi distribusi RF. Tidak ada modul game yang telah diimplementasikan.

## Identitas

| File | Ukuran byte | Header PE | Machine | Temuan |
| --- | ---: | --- | --- | --- |
| ODZone.exe | 10457088 | PE32+ | 0x8664 (x64) | GUI, 8 section, impor ODGuard.dll |
| ZoneServerUD_x64.exe | 83968 | PE32 | 0x014c (x86) | GUI, section UPX0 / UPX1 / .rsrc; `file` mengidentifikasi UPX |

SHA-256:

```text
ODZone.exe
5918e46a6f49814d4222cd7a60a01a09a630b5e2ad6b5a2844a26cd2a7d3f44f

ZoneServerUD_x64.exe
b5c4095c89773acdf18b455074a4f33473795937ec3480bd2b46c0dd399e7940
```

## ODZone.exe: fakta

- Section: `.text`, `.rdata`, `.data`, `.pdata`, `.idata`, `.didat`, `.rsrc`, `.NewIT`.
- COFF timestamp: 2009-08-07 11:36:43 UTC. Bukan bukti tanggal rilis atau versi game.
- PE entry-point RVA: `0x4dd320`; preferred ImageBase: `0x140000000`. Ini metadata, bukan alamat hook yang disetujui.
- Import directory RVA `0x44afe000`, ukuran 460 byte, berada dalam `.NewIT`. Daftar impor diperiksa dengan pemetaan RVA ke offset file; output `objdump -p` sendiri tidak menampilkan nama DLL ODZone secara lengkap.
- Import descriptor menyebut: NETAPI32.dll, ODBC32.dll, WS2_32.dll, WINMM.dll, DDRAW.dll, d3dx9_30.dll, MSVCP80D.dll, MFC80D.DLL, MSVCR80D.dll, KERNEL32.dll, USER32.dll, GDI32.dll, ADVAPI32.dll, ole32.dll, OLEAUT32.dll, AntiCpSvr.dll, RFACC.dll, WININET.dll, dbghelp.dll, MSVCP80.dll, comdlg32.dll, ODGuard.dll.
- Nama `ODGuard.dll` ditemukan pada offset file `0x9f8fcc` dan dirujuk oleh import descriptor. Ini bukti dependensi langsung, bukan bukti fitur atau validitas lisensi.
- Terdapat string `ZoneServer_MainLoop` pada offset `0x76aa30`, pesan konfigurasi World/Cash ODBC, dan jalur log ZoneServer.
- Ada string jalur debug yang berakhir `ZoneServerUD_x64.pdb` pada offset `0x8ba77c`. Ini bukan file PDB yang disertakan, bukan source code, dan tidak membuktikan executable lain dengan nama serupa identik.

## ODZone.exe: implikasi dan ketidakpastian

Penanda ZoneServer dan dependensi ODBC/socket mendukung dugaan bahwa ini executable server yang sudah terintegrasi komponen guard. Peran semua impor, hubungan pemanggilan ODGuard, ABI dan alur startup belum ditelusuri.

Impor runtime debug VC80 (`MSVCP80D`, `MFC80D`, `MSVCR80D`) harus diperhitungkan saat menyiapkan lingkungan uji; belum diverifikasi tersedia. Belum ada dasar untuk mengganti DLL dengan stub, menghapus dependensi guard, mengubah pemeriksaan lisensi, atau menebak ABI.

## ZoneServerUD_x64.exe: fakta dan batas

- Nama file mengandung x64, tetapi header menyatakan x86. Nama file tidak dapat dijadikan acuan arsitektur.
- Section `UPX0`, `UPX1`, `.rsrc` menunjukkan karakteristik packing UPX. File belum di-unpack.
- Impor yang terlihat: KERNEL32.DLL, COMCTL32.dll, GDI32.dll, MSVCRT.dll, OLE32.dll, SHELL32.dll, USER32.dll.
- Impor KERNEL32 yang terlihat mencakup LoadLibraryA, GetProcAddress dan VirtualAlloc; SHELL32 memuat ShellExecuteExA. Impor ini tidak membuktikan program adalah launcher, loader tertentu, atau memiliki perilaku berbahaya.
- COFF timestamp: 2009-02-07 13:33:08 UTC; entry-point RVA `0x1d050`.
- Peran sebenarnya dan hubungan terhadap ODZone belum dibuktikan. Impor file packed tidak dapat dianggap daftar dependensi kode asli yang lengkap.

## Keputusan pengembangan

1. Jangan menganggap kedua executable dapat saling menggantikan. Arsitekturnya berbeda.
2. Pertahankan status 19 komponen sebagai pending: belum ada spesifikasi lengkap maupun titik integrasi yang terverifikasi.
3. Prioritaskan identifikasi dependensi dan baseline server sebelum modifikasi gameplay.
4. Untuk integrasi baru, utamakan source/SDK atau baseline server yang memang ditujukan untuk pengembangan; jangan membuat pengganti ODGuard dengan asumsi ABI.

## Bahan berikutnya

- Daftar nama file `.exe`/`.dll` di `F:\SERVER\SERVER\ZoneServer\RF_Bin` dan isi folder `ODGuard`/`PROTECT` berupa daftar nama, bukan kredensial.
- Source/SDK dan PDB yang sesuai jika tersedia; cukup konfirmasi keberadaannya dulu.
- File executable client RF yang cocok, serta bukti baseline dapat login.
- Dokumentasi aturan modul yang belum tercantum dalam tiga PDF instalasi.

Repository publik: jangan tambahkan konfigurasi database, token, dump atau data pemain. File tambahan pihak ketiga dapat dikirim privat di chat untuk analisis jika diperlukan.
