# Dokumentasi referensi dan rancangan awal

## Bukti yang tersedia

Sumber: tiga PDF dari pengguna, diekspor dari dokumentasi OwnDev pada 23 Oktober 2026: Requirements, Database, dan Common Errors. Catatan ini merupakan ringkasan, bukan source code atau spesifikasi lengkap produknya.

Requirements menyebut SQL Server + SSMS, server standar 2.2.3.2, ZoneServer berjalan tanpa error dan login standar berhasil sebelum menerapkan patch.

Database menjelaskan produk referensi memuat migrasi melalui SnooperGS.dll ketika ZoneServer dimulai. Main.ini memetakan ODBC_World, ODBC_User, ODBC_Billing; DatabaseMigration.ini memetakan skrip ke database. Status migrasi disimpan agar perubahan tidak berulang. Log muncul saat ada perubahan atau error. Ini perilaku produk referensi, bukan implementasi proyek ini.

Dokumen menyebut SQL Server 2014-2019 sebagai rentang rekomendasi kompatibilitas produknya; proyek belum menguji versi SQL Server mana pun. Jangan menganggap rekomendasi tersebut sebagai penilaian dukungan/security lifecycle terkini.

Migrasi referensi dapat mengubah kolom tbl_base dan collation billing. Jika beberapa ZoneServer berbagi World database, dokumentasi meminta satu instance melakukan migrasi lebih dahulu. Reset Season Pass tidak mencadangkan data secara otomatis. Jangan menjalankan reset/migrasi pada database produksi sebagai bagian inventaris.

Common Errors mencantumkan masalah IP publik, database, registrasi, migrasi, versi client, kelengkapan patch, serta prosedur/ODBC Billing. Isi solusi accordion tidak tercetak lengkap dalam PDF.

## Rancangan proyek (usulan, belum terimplementasi)

| Bagian | Tanggung jawab yang perlu dibuktikan |
| --- | --- |
| Client | UI, input pengguna dan tampilan status; kebutuhan tiap fitur belum ditentukan |
| Server | Validasi otoritatif aturan gameplay, kepemilikan item dan transaksi |
| Database | Penyimpanan progres, audit dan migrasi sesuai skema aktual |
| Packaging | Manifest file, verifikasi checksum, petunjuk instalasi dan pemulihan |

Lokasi integrasi, ABI, struktur object, format paket, loader dan arsitektur binary belum diketahui. Nama DLL/path pada produk referensi tidak menetapkan desain atau kompatibilitas proyek ini.

## Data yang belum tersedia

- Lokasi dan identitas file client/server pengguna; source code atau SDK jika ada.
- Versi/arsitektur yang dibuktikan dari file dan keadaan server standar.
- Rincian perilaku seluruh fitur, konfigurasi, UI dan aturan transaksi.
- Skema database yang sudah disanitasi dan hubungan Billing/User/World aktual.
- Lingkungan uji, compiler/toolchain, dan mesin analisis native yang tersedia.

## Kriteria sebelum distribusi

Build nyata, uji client/server pada target, migrasi pada salinan database, pencegahan klaim hadiah/transaksi ganda, pengujian restart dan kegagalan, serta prosedur pemulihan yang diuji. Kapasitas pemain membutuhkan uji beban terpisah; angka dari paket referensi bukan jaminan.
