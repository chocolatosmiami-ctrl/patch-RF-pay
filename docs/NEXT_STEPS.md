# Mulai dari laptop dengan Codex + REA

## Prasyarat yang sudah dikonfirmasi dalam percakapan

Windows x64; Node.js 24.14.0; REA 6.7.0. MCP REA telah merespons panggilan binary_session pada sesi Codex pengguna. Ini tidak membuktikan mesin analisis native sudah dikonfigurasi atau file RF sudah diperiksa.

## Langkah awal

1. Clone repository ini melalui Git atau GitHub Desktop dan buka foldernya di Codex lokal.
2. Berikan lokasi folder client dan server RF yang sebenarnya. F:\rea-main adalah folder source REA yang diunduh, bukan lokasi RF yang sudah dikonfirmasi.
3. Jalankan alat inventaris sesuai README jika Python tersedia. Alternatifnya, minta Codex melakukan inventaris setara secara read-only di laptop.
4. REA memeriksa header/file target untuk membuktikan identitas dan kebutuhan provider. Bila perlu dekompilasi native, konfigurasikan provider yang didukung versi REA terpasang sebelum melanjutkan.
5. Periksa bahwa baseline server berjalan dan login berhasil di lingkungan uji. Jangan menganggap pemeriksaan static cukup.
6. Lengkapi aturan fitur; mulai satu modul yang memiliki spesifikasi dan titik integrasi terbukti.

## Instruksi yang dapat dikirim ke Codex lokal

```text
Baca README.md, AGENTS.md, docs/FEATURES.md dan docs/ARCHITECTURE.md.
Mulai pengembangan patch RF melalui MCP REA yang tersedia.
Minta lokasi client/server jika belum diketahui, lalu lakukan inventaris statis:
nama file, ukuran, SHA-256, arsitektur PE dan bukti versi yang tersedia.
Jangan jalankan executable, edit file game, sambungkan database, atau tampilkan kredensial saat inventaris.
Periksa kemampuan/provider REA yang benar-benar tersedia.
Pisahkan fakta hasil analisis dari usulan. Jangan mengarang offset atau struktur paket.
Laporkan titik integrasi yang terbukti dan hambatan sebelum implementasi modul pertama.
Simpan laporan mentah lokal di local-reports/; commit hanya catatan teknis yang sudah disanitasi.
```

## Informasi yang masih dibutuhkan dari pemilik

- Folder dan versi RF client/server; apakah ada source code/SDK.
- Apakah baseline dapat login.
- Dokumentasi detail perilaku modul; tiga PDF awal belum memuatnya.

Tidak diperlukan password atau dump data pemain untuk tahap ini.
