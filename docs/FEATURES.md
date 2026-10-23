# Cakupan fitur

Daftar berikut berasal dari screenshot pilihan pengguna. Seluruh komponen masih **menunggu spesifikasi dan analisis target**. Nama tidak membuktikan perilaku atau cara implementasinya.

| No. | Komponen | Hal yang harus ditentukan |
| --- | --- | --- |
| 1 | Basic Type 2 (Max login 2.532 Players) | Arti paket dasar dan kapasitas belum dispesifikasikan atau diuji. |
| 2 | Dungeon Time | Aturan waktu, reset, map dan penyimpanan belum diketahui. |
| 3 | Potion Kill | Pemicu, efek dan interaksi combat belum diketahui. |
| 4 | Tower License | Hak penggunaan, syarat, durasi dan validasi belum diketahui. |
| 5 | Guild Point | Sumber poin, pemakaian, reset dan hak guild belum diketahui. |
| 6 | Infinite Potion | Jenis item, konsumsi, cooldown dan batas penggunaan belum diketahui. |
| 7 | Player Inspector | Data yang terlihat, UI dan aturan akses belum diketahui. |
| 8 | Asset Encrypt | Format aset, loader, algoritme dan pengelolaan kunci belum diketahui. |
| 9 | Broadcast Message | Pemicu, penerima, format, frekuensi dan UI belum diketahui. |
| 10 | Looting Magnet | Radius, kepemilikan drop, filter dan batas inventory belum diketahui. |
| 11 | War Battle | Aturan event, scoring, hadiah dan jadwal belum diketahui. |
| 12 | Player Aura | Efek visual, syarat aktivasi dan sinkronisasi belum diketahui. |
| 13 | 7-Day VIP Login | Definisi hari, VIP, hadiah, reset dan klaim belum diketahui. |
| 14 | Guild Skill | Daftar skill, biaya, level, efek dan persistensi belum diketahui. |
| 15 | Auction Cash | Aturan lelang, mata uang, fee dan settlement belum diketahui. |
| 16 | Enchant Protector | Efek perlindungan, probabilitas, konsumsi dan kegagalan belum diketahui. |
| 17 | AutoMine Manager | Aturan penambangan, eligibility, reward dan durasi belum diketahui. |
| 18 | Transfer Limit | Objek transfer, periode, batas dan pengecualian belum diketahui. |
| 19 | Season Pass | Misi, progres, tier, premium, hadiah dan pergantian musim belum diketahui. |

## Status dan kriteria selesai

`pending_specification` -> `specified` -> `implemented` -> `integration_tested` -> `released`. Perubahan status harus disertai spesifikasi, kode dan bukti sesuai tahap. `enabled: false` pada katalog bukan konfigurasi RF yang dapat langsung digunakan.

Untuk setiap modul: tentukan perilaku, client/server yang berubah, penyimpanan, validasi otoritatif, skenario gagal, pengujian dan rollback. Basic Type 2 adalah label paket referensi dan perlu diuraikan menjadi kebutuhan teknis; bukan modul dengan jaminan 2.532 pemain.
