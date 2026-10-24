# patch-RF-pay

Proyek pengembangan modul RF Online dengan implementasi sendiri. REA digunakan untuk analisis file lokal dan pembuktian kompatibilitas.

## Status

**Tahap awal: spesifikasi dan inventarisasi. Belum ada patch game atau DLL siap pakai.** Tidak ada modul yang dinyatakan selesai, batas pemain yang telah diuji, atau kompatibilitas client/server yang sudah dibuktikan.

Target referensi dokumentasi adalah RF server **2.2.3.2**; versi distribusi file pengguna belum terbukti. ODZone/SnooperGS EXE telah diidentifikasi x64; identifikasi ini tidak membuktikan versi RF atau kesiapan runtime. Basic Type 2 / 2.532 pemain adalah label paket referensi, bukan hasil uji kapasitas proyek ini.

- [Studi cara menjalankan server dan verifikasi baseline](docs/SERVER_RUNBOOK.md)
- [Studi enam repository pada topik rfonline](docs/GITHUB_RFONLINE_STUDY.md)
- [Cakupan 19 komponen](docs/FEATURES.md)
- [Analisis dokumentasi dan rancangan awal](docs/ARCHITECTURE.md)
- [Langkah berikutnya dengan Codex dan REA](docs/NEXT_STEPS.md)
- [Katalog status yang dapat dibaca program](config/features.json)

## Inventaris file RF lokal

Alat ini hanya membaca file `.exe` dan `.dll`, mencatat ukuran, SHA-256 dan arsitektur PE. Tidak menjalankan game, mengubah file RF, membaca konfigurasi database, atau mengunggah laporan. Python 3.9+ diperlukan untuk alat inventaris; bukan persyaratan runtime RF.

Di CMD, dari folder repository (ganti lokasi contoh dengan folder asli):

```cmd
py -3 tools\inventory_rf.py --root "F:\RF-Client" --label client --output "local-reports\client.json"
py -3 tools\inventory_rf.py --root "F:\RF-Server" --label server --output "local-reports\server.json"
```

Laporan disimpan lokal dan diabaikan Git. Alat melewati symlink/junction dan tidak membaca isi INI, SQL, database, atau data pemain. Kesalahan akses akan tercatat dan menghasilkan exit code 2. Verifikasi versi game tetap membutuhkan analisis lanjutan; arsitektur PE bukan versi RF.

## Cara kerja pengembangan

1. Periksa client/server standar dan bukti login berhasil.
2. Lengkapi aturan perilaku setiap fitur dari dokumentasi dan kebutuhan pemilik server.
3. Identifikasi integrasi yang tersedia pada source atau binary yang diperiksa dengan REA.
4. Implementasikan modul bertahap pada salinan pengujian.
5. Build dan uji sebelum menghasilkan paket distribusi.

Belum ada GitHub Release. Arsip source repository ini bukan patch yang dapat dipasang ke game.

## Isi repository

Source proyek, konfigurasi contoh, dokumentasi, dan tooling. Jangan commit client/server lengkap, binary pihak ketiga, dump database, kredensial, atau data pemain. Tidak ada kode OwnDev yang disalin ke proyek ini.

## Pemeriksaan lokal

```cmd
py -3 -m unittest discover -s tests -v
```

Pengujian saat ini hanya memverifikasi alat inventaris, bukan gameplay atau integrasi RF.
