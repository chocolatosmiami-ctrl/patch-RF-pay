# Studi cara menjalankan paket server RF

Tanggal: 24 Oktober 2026. Acuan repository saat studi: commit 7ace03da903b0d0e9562c5ed4c2ae09ff2b7ef96. Status: studi statis dan rencana verifikasi; server belum dijalankan.

## 1. Ringkasan yang sudah diketahui

Server ini adalah kumpulan komponen, bukan satu EXE yang cukup diklik. Executable ZoneServer memerlukan DLL, data game, konfigurasi, koneksi database, dan koneksi ke komponen akun. Client yang cocok diperlukan untuk membuktikan login dan gameplay.

Bukti yang dipakai:
- Dua executable dalam repository: ODZone.exe dan ZoneServerUD_x64.exe.
- SnooperGS.exe, SnooperGS.dll, ReadMe, tiga PDF dokumentasi dan delapan INI dari pengguna di chat.
- Screenshot direktori server. Folder lokal yang sudah terlihat: F:\SERVER\SERVER\ZoneServer\RF_Bin.
- Analisis pada BINARY_ANALYSIS.md, SNOOPER_ANALYSIS.md, PACKAGE_README_ANALYSIS.md dan CONFIG_ANALYSIS.md.
- Dokumentasi Microsoft ODBC yang ditautkan di bawah.

Tidak ada source gameplay RF, executable Account/Login/Control, backup/skema database lengkap atau client executable yang tersedia dalam repository pada commit acuan. Folder bernama Account,Login atau Database pada screenshot bukan bukti bahwa seluruh isinya lengkap atau dapat berjalan.

## 2. Peta komponen dan bukti

| Komponen | Apa yang diketahui | Belum diketahui |
| --- | --- | --- |
| SQL Server | PDF mensyaratkan SQL Server dan SSMS; World/User/Billing dipetakan lewat ODBC pada dokumentasi guard | Instance, nama database aktual, driver, schema, credential dan keadaan restore |
| Account/Login | Screenshot memuat folder Account,Login; ODZone memiliki pesan gagal koneksi Account Server | Executable, file config, port, urutan startup dan protokol paket |
| Control/Manage | Screenshot memuat ControlServer&ManageTool | Fungsi operasional dan apakah wajib untuk build ini |
| ZoneServer | ODZone dan SnooperGS EXE yang diperiksa x64; ada rujukan data game dan ODBC | Versi distribusi RF yang tepat, baseline login dan kesiapan runtime |
| Guard | ODZone meminta ODGuard.dll; SnooperGS meminta SnooperGS.dll; ordinal tersedia pada DLL Snooper | Cara inisialisasi internal, semua aturan fitur dan perilaku runtime |
| Client | GM.ini merujuk file client Snooper/mod/gm.ini | Binary, build, patch, data, alamat koneksi dan kesesuaian protokol |
| Data game | Screenshot memperlihatkan Script, luaScript, Initialize, Map, WorldInfo dan SystemSave | Kelengkapan file dan kecocokan datanya dengan EXE/client |

## 3. Bukti tambahan dari ODZone.exe

Penanda ASCII ditemukan pada offset file berikut. Ini referensi statis, bukan jejak eksekusi atau bukti semua cabang berjalan saat startup.

| Offset | Penanda | Kesimpulan terbatas |
| --- | --- | --- |
| 0x7697f0 | Account Server Connectting Fail : %d | Ada jalur yang melaporkan kegagalan koneksi Account Server |
| 0x7549c0 | ServerType is Wrong ==> AccountServer(%d) != ZoneServer(%d) | Ada penanda pemeriksaan kecocokan tipe server |
| 0x76ee20 | World DB ODBC Setting Faild! | Ada jalur pelaporan kegagalan World ODBC |
| 0x76ee50 | World DB ODBC Config Complete!! | Ada penanda keberhasilan konfigurasi World ODBC |
| 0x7cfa10 | Cash DB ODBC Setting Failed! | Ada jalur pelaporan kegagalan Cash ODBC |
| 0x6fad60 | .\\Initialize\\WorldSystem.ini | Binary merujuk konfigurasi WorldSystem |
| 0x709278 | .\\Script\\SystemGuardTower.ini | Binary merujuk script GuardTower |
| 0x76ac88 | ..\\ZoneServerLog\\Systemlog\\SystemError%d.log | Ada pola nama log error |
| 0x76acb8 | ..\\ZoneServerLog\\Systemlog\\LoadingProcess.log | Ada pola log proses loading |
| 0x84e8c8 | bind() Failure => %d | Ada jalur error bind socket |
| 0x84e8e0 | listen() Failure => %d | Ada jalur error listen socket |

Referensi path mendukung kebutuhan mempertahankan susunan folder. Working directory dan cara aplikasi menyusun path perlu diverifikasi pada test machine; jangan memindahkan EXE sendirian atau menganggap semua API INI memakai aturan pencarian path yang sama.

## 4. Persiapan menjalankan server: urutan dependensi

Ini urutan persiapan berbasis prasyarat, BUKAN urutan klik executable yang sudah diuji:

1. Identifikasi paket: pilih baseline/build yang konsisten, catat hash, pisahkan salinan uji dan pertahankan struktur direktori. Jangan mencampur ODGuard dengan SnooperGS berdasarkan nama atau ukuran.
2. Siapkan database sesuai paket pada SQL Server; cocokkan World/User/Billing dan schema pada salinan uji. SSMS adalah alat pengelolaan, bukan pengganti layanan SQL Server.
3. Cocokkan ODBC driver dan DSN dengan arsitektur tiap proses. Uji koneksi DSN secara lokal di test machine; jangan mengirim password ke repository.
4. Periksa DLL runtime/dependensi yang benar untuk build. Impor debug VC80 pada ODZone/SnooperGS perlu diselesaikan melalui lingkungan/toolchain yang sesuai; memasang redistributable biasa belum membuktikan semua runtime debug tersedia.
5. Cocokkan alamat, tipe server, endpoint dan port komponen berdasarkan konfigurasi aktual. Angka port dan DSN tidak boleh ditebak dari tutorial paket lain.
6. Pastikan komponen pendukung yang dibutuhkan ZoneServer sudah siap menerima koneksi. Urutan persis Account/Login/Control harus diambil dari konfigurasi/panduan paket tersebut; file yang ada sekarang belum membuktikannya.
7. Jalankan hanya pasangan ZoneServer/guard yang sesuai pada test machine, dengan data dan konfigurasi paket lengkap. Baca log loading, database, koneksi dan error.
8. Uji client yang cocok: login, pilih/buat karakter, masuk map, lalu uji simpan dan login kembali.
9. Setelah baseline lulus, ubah satu fitur per percobaan; catat config, hasil gameplay dan persistensi. Baru susun paket patch hasil pengembangan.

Tidak ada langkah di atas yang dijalankan oleh studi ini. Tidak dibuat start-all.bat karena nama proses pendukung, argumen, kesiapan koneksi dan working directory seluruh paket belum diverifikasi.

## 5. ODBC 32-bit versus 64-bit

Microsoft menyatakan aplikasi dan driver ODBC harus cocok arsitekturnya. Di Windows x64:
- Administrator ODBC 64-bit: C:\Windows\System32\odbcad32.exe.
- Administrator ODBC 32-bit: C:\Windows\SysWOW64\odbcad32.exe.
- System DSN 32-bit dan 64-bit terpisah; User DSN yang terlihat pada kedua alat tidak membuktikan drivernya cocok.

Implikasi untuk paket: ODZone.exe dan SnooperGS.exe yang diperiksa membutuhkan jalur driver ODBC x64. Jangan memilih berdasarkan nama file: ZoneServerUD_x64.exe yang diunggah justru PE x86 dan perannya belum terbukti. Arsitektur proses Account/Login belum tersedia, jadi tidak dapat dianggap semuanya x64.

Sumber Microsoft:
- https://learn.microsoft.com/en-us/troubleshoot/sql/connect/odbc-tool-displays-32-bit-64-bit
- https://learn.microsoft.com/en-us/sql/odbc/admin/viewing-drivers?view=sql-server-ver15

## 6. Dua prosedur database yang harus dipisahkan

ReadMe paket pengguna menyebut SQL addon manual BILLING, NEW_FIX_2022 dan POTION_SAVE. PDF Database menyebut migrasi otomatis melalui DatabaseMigration.ini dan PROTECT/Database saat ZoneServer mulai.

Jangan menjalankan keduanya sekaligus berdasarkan asumsi. File DLL Snooper memiliki penanda proteksi dan lisensi, tetapi pembacaan statis ini belum membuktikan metode migrasi mana yang digunakan build tersebut. Isi SQL dan kecocokan build harus diperiksa sebelum perubahan database.

Jika menggunakan build yang migrasinya otomatis, startup sendiri dapat mengubah schema. Baseline pertama harus memakai database uji yang dapat dipulihkan. Reset Season Pass pada PDF tidak membuat backup otomatis.

## 7. Tanda keberhasilan dan pelacakan masalah

| Tahap | Bukti keberhasilan yang harus dikumpulkan | Bila gagal, periksa |
| --- | --- | --- |
| Database | Koneksi instance dan DSN berhasil pada arsitektur proses yang tepat | Layanan SQL, driver, DSN, mapping database, hak akses |
| Pendukung akun | Log/proses menyatakan siap dan koneksi Zone diterima | Endpoint, port, tipe server dan dependensi aktual |
| Loading Zone | Data selesai dimuat tanpa error fatal | Kelengkapan Initialize/Script/Map/DLL dan working directory |
| Guard | Startup sesuai paket tanpa error konfigurasi/lisensi | Pasangan EXE/DLL, config dan hak penggunaan; tidak membypass batas lisensi |
| Client | Login sampai masuk dunia game | Build/protokol, patch client, endpoint dan log server |
| Persistensi | Perubahan uji tersimpan setelah relog dan restart terkontrol | Schema, transaksi, save path dan kegagalan database |

Sekadar jendela EXE terbuka tidak berarti server siap. File log lama tahun 2019 pada screenshot tidak membuktikan kondisi saat ini.

## 8. Alur fitur yang dipakai untuk desain nanti

Model desain yang akan diuji: aksi pemain -> validasi otoritatif pada server -> perubahan state/transaksi -> persistensi -> respons ke client. Ini rancangan, bukan hasil dekompilasi lengkap.

INI adalah masukan konfigurasi. Menyalin nama key tidak membuat handler server, UI client, transaksi atau migrasi. Untuk setiap modul diperlukan aturan perilaku, tempat integrasi yang terbukti, dan skenario gagal. Dungeon/Guild Point/Guild Skill baru memiliki spesifikasi parsial; tabel enchant tidak boleh diubah menjadi persentase tanpa rumus/skala RNG yang terbukti.

## 9. Kesimpulan kesiapan

Sudah dipahami dari bukti: identitas arsitektur target, pasangan EXE/DLL, jalur dependensi database/Account Server, beberapa rujukan data game, dan sebagian parameter modul.

Belum dipahami sampai tingkat implementasi: protokol client/server, urutan lengkap Account/Login/Control, schema aktual, titik handler/hook fitur, ABI, serta seluruh aturan produk referensi. Studi yang ada cukup untuk menyusun rencana baseline; belum cukup untuk menjamin menjalankan seluruh server atau menghasilkan semua modul.

Dokumen ini menjadi catatan proyek agar pemeriksaan berikutnya tidak mengulang temuan yang sama. Tidak ada klaim kerja latar belakang atau server yang sedang berjalan.
