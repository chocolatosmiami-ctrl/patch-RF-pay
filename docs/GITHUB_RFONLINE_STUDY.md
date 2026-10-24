# Studi GitHub Topics rfonline

Tanggal peninjauan: 24 Oktober 2026. Titik awal: https://github.com/topics/rfonline

## Cakupan pemeriksaan

Halaman topik yang ditinjau menampilkan enam repository. README keenamnya, daftar file root, metadata lisensi GitHub, dan source terpilih diperiksa. Tidak ada aplikasi yang diinstal, dibangun, dijalankan, atau dipasang ke client/server RF pengguna.

Kesimpulan dibatasi pada enam repository yang tampil saat pemeriksaan, bukan seluruh proyek RF Online di GitHub. GitHub Topics bukan SDK atau dokumentasi resmi RF. Klaim README dibedakan dari isi kode yang diperiksa.

## Ringkasan repository

| Repository | Jenis | Bukti yang diperiksa | Kegunaan untuk proyek |
| --- | --- | --- | --- |
| [tommyhawkdev/RFAutoLoot](https://github.com/tommyhawkdev/RFAutoLoot) | Otomasi input client C#/WinForms | README, tree, AutoLoot.cs, Utilities.cs dan AutoLoot.cs varian Client | Contoh pemilihan proses, window handle, timer dan input; bukan implementasi loot magnet server |
| [iffardamahum/RF-Memory-Scanner](https://github.com/iffardamahum/RF-Memory-Scanner) | Pembaca memori client Python | README, RF.py, root | Contoh observasi object client; offset penting berasal dari environment yang tidak disertakan |
| [xuevertalex-web/RFMapToolMain](https://github.com/xuevertalex-web/RFMapToolMain) | Alat map/aset C# .NET 8 | README, tree lengkap, MapLoader.cs, MapScene.cs, csproj | Referensi kategori format map dan pemisahan parser/exporter; kesiapan build belum dibuktikan |
| [josemumuchan/rfemblemeditor](https://github.com/josemumuchan/rfemblemeditor) | Editor emblem SPR/DDS di browser | README, index.html dan parser SPR/DXT1 | Referensi struktur SPR varian yang dipakai alat serta alur edit/simpan emblem |
| [josemumuchan/rfsentinel](https://github.com/josemumuchan/rfsentinel) | Companion client AFK/MAU | README dan root repository | Deskripsi monitoring HP dan pemicu input; root yang diperiksa hanya berisi README, bukan source implementasi |
| [wyrtensi/rfonline-vkplay-bellato-cora-mod](https://github.com/wyrtensi/rfonline-vkplay-bellato-cora-mod) | Patcher aset client Python | README, tree root, struktur fungsi source serta BackupManager/RFSHandler | Referensi backup-manifest, rollback dan archive RFS; target yang dinyatakan adalah client RF 4.75, bukan baseline server 2.2.3.2 |

## 1. RFAutoLoot bukan Looting Magnet server

Varian Client memakai Process.GetProcessesByName, PID, MainWindowHandle, timer WinForms dan SendMessage untuk tombol X. Ini otomatisasi aksi client. Tidak terlihat implementasi server untuk radius loot, kepemilikan drop, pemindahan inventory atau transaksi.

Source varian single yang diperiksa juga tidak sama dengan varian Client; kesiapan build semua varian belum diuji. Jangan menganggap README dan semua folder merupakan satu implementasi siap pakai.

Implikasi: fitur Looting Magnet yang direncanakan tetap membutuhkan handler loot otoritatif pada server; menekan tombol X berkala bukan penggantinya.

## 2. RF-Memory-Scanner adalah observasi client

RF.py memuat BASE_PTR dan offset dari environment, lalu membaca object pada proses RF_Online.bin dengan pymem. Loop membaca nama, jarak, state dan ID. Kode yang diperiksa melakukan pembacaan memori, bukan menyediakan source ZoneServer atau menambah kapasitas server.

Offset tidak tersedia sebagai spesifikasi target pengguna. Pola pembacaan object 4-byte juga tidak membuktikan cocok dengan semua build/client atau server x64 yang kita periksa.

## 3. RFMapToolMain: manfaat dan keterbatasan

README menjelaskan map BSP/EBP, material R3M, tekstur R3T, object SPT/RVP dan ekspor GLB. MapLoader.cs benar-benar menyusun path map, memanggil loader format-format tersebut, dan membangun MapScene. csproj menyebut net8.0 dan library grafis terkait.

Ada perbedaan antara README dan tree publik yang diperiksa: README menyebut direktori Parsing, tetapi direktori tersebut tidak terlihat pada tree lengkap. MapLoader dan MapScene merujuk tipe pada namespace Collision, Materials, Textures, Spt dan Rvp. Tidak dilakukan build, jadi laporan ini tidak menyimpulkan error build tertentu atau kelengkapan parser dari README saja.

Implikasi: ini referensi pengolahan aset dan kategori format; bukan bukti ada SDK server, schema database atau protokol login.

## 4. RF Emblem Editor: struktur data yang dapat dipelajari

index.html memuat parser dan writer SPR serta decoder/encoder DXT1. Varian SPR yang dipakai alat memiliki header 12 byte dan descriptor tekstur 24 byte, diikuti payload tekstur. DataView memakai little-endian. Ini observasi terhadap implementasi alat, bukan jaminan format seluruh file .spr RF.

Penggunaan untuk proyek: analisis dan validasi aset client, terutama emblem/UI. Belum ada file SPR pengguna yang diperiksa atau diuji round-trip.

## 5. RF Sentinel: batas bukti source

README menjelaskan pemilihan PID, pymem, pointer/AoB untuk HP dan pemicu tombol ketika HP melewati ambang. Daftar root yang diperiksa hanya README; tidak ada source yang dapat mengonfirmasi detail algoritme runtime. Tidak ada binary release yang diunduh atau dijalankan.

Implikasi: referensi konsep alat pendamping client, bukan source modul server atau anti-cheat.

## 6. Patcher Cora/Bellato: pelajaran packaging

Source cora_bellato_patcher.py memuat BackupManager, RFSHandler, SpritePatcher, SkeletonAdapter dan AssetSwapper.

Bagian yang diperiksa langsung:
- BackupManager menyalin file ke folder backup dan menyimpan manifest ukuran/hash MD5.
- Rollback mengembalikan file; beberapa jalur menghapus direktori dan cache. Ini perlu review sebelum penggunaan, bukan otomatis aman hanya karena ada backup.
- RFSHandler membaca jumlah entri 32-bit little-endian, tabel entri 64-byte dengan nama, metadata, offset dan ukuran; writer membangun ulang archive.
- Target versi 4.75 disebut README. Tidak ada bukti format atau aturan ini cocok dengan client pengguna.

Pelajaran untuk implementasi sendiri: manifest berbasis hash, pemeriksaan target sebelum perubahan, backup yang diverifikasi dan rollback yang diuji. Jangan menyalin operasi penghapusan/penulisan tanpa pembatasan path, validasi backup dan uji pada salinan. Proyek kita belum membuat patcher game berdasarkan kode ini.

## Lisensi dan penggunaan kode

Metadata GitHub mengidentifikasi RFAutoLoot sebagai GPL-3.0 dan patcher Cora/Bellato sebagai MIT. Empat repository lain tidak menampilkan lisensi yang terdeteksi pada metadata saat pemeriksaan. Nilai null tidak membuktikan tidak ada ketentuan lain; file/izin perlu diperiksa sebelum reuse.

Tidak ada source pihak ketiga yang disalin ke patch-RF-pay dalam studi ini. Membaca kode publik tidak otomatis menjadikan seluruh implementasi/aset boleh didistribusikan.

## Hubungan dengan target patch-RF-pay

| Target kita | Dukungan dari topik ini |
| --- | --- |
| Kapasitas 2532 pemain | Tidak ditemukan implementasi server yang mendukung perubahan kapasitas pada keenam repo; temuan LimUserNum sebelumnya tetap bukti utama |
| Dungeon Time / Tower License / Guild Point | Tidak ditemukan handler ZoneServer atau SDK untuk memasang modul ini |
| Looting Magnet | Ada contoh autoloot input client; semantik dan integrasi berbeda |
| Player Inspector | Ada pembacaan object client; belum menyediakan API/UI inspector dan validasi server |
| Asset Encrypt | Ada parser/editor/patcher aset; tidak ditemukan implementasi enkripsi aset dan loader pasangan yang cocok |
| UI, emblem, map, distribusi patch | Referensi paling relevan dari studi ini |
| Cara menjalankan seluruh server RF | Keenam repo belum memberi paket lengkap Account/Login/Zone/database yang cocok dengan file pengguna |

## Keputusan teknis

1. Pertahankan desain modul server dan alat client sebagai komponen terpisah.
2. Jangan mengadopsi offset, protokol, parser atau patch RF 4.75 ke target lain tanpa file dan uji kompatibilitas.
3. Gunakan studi ini untuk memahami kategori aset dan rancangan packaging; jangan menyatakan semua fitur OwnDev siap dibuat hanya dari enam repository.
4. Tahap berikutnya tetap membuktikan baseline server/client dan titik integrasi. Source/SDK server yang cocok belum ditemukan pada halaman topik ini.
5. Semua modul gameplay proyek tetap belum dirilis; studi ini tidak mengubah status kapasitas menjadi teruji.
