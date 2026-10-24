# Pemetaan delapan konfigurasi referensi

Tanggal: 24 Oktober 2026. Sumber: delapan INI yang diunggah pengguna. Analisis hanya membaca teks dan memeriksa bentuk tabel. Tidak ada konfigurasi, binary atau database yang diubah. Nilai Discord, hak akses GM dan identitas perangkat tidak dipublikasikan. File asli tidak disalin ke repository.

## Aturan yang tertulis

| File | Fakta dari nilai/komentar | Batas kesimpulan |
| --- | --- | --- |
| Dungeon_Timer.ini | Enable=false; dua interval 08:01-10:00 dan 21:01-22:00; komentar membatasi waktu masuk dungeon dan menyebut auto reload | Jadwal akses, bukan durasi sesi. Zona waktu, inklusivitas batas, interval lintas tengah malam dan efek pada pemain di dalam belum dijelaskan |
| Enchant.ini | JewelRate=0.125, AutoSetMaterials=true; seluruh flag notifikasi yang diberikan false; tabel ItemSave, ItemDestroy, ItemDowngrade | Rumus peluang, skala RNG, urutan evaluasi dan makna JewelRate belum dibuktikan |
| GM.ini | Notifikasi login GM aktif; komentar menunjuk teks client Snooper/mod/gm.ini; akses per jenis perintah melalui grade/sub; komentar menyebut ambang greater-or-equal dan auto reload | Nilai ambang tidak dipublikasikan. Penggabungan grade/sub dan otorisasi aktual belum ditelusuri |
| Guild.ini | Level masuk minimum 30; biaya guild 24000000; biaya emblem 3000000; GvG MAX_REGIST=1 dan MIN_SUGGESTING_GRADE=3; HonorGuild FIX=false | Mata uang, cakupan batas registrasi dan efek FIX=false belum dijelaskan penuh. Komentar hanya menyebut FIX=true untuk original guild |
| Guild_Point.ini | Enable=false; penambahan dari PvP, CPT dan TotalPlayTime diset true dengan komentar 1:1; hanya menambah; potion custom type 177 melalui PotionReplaced; AutoSetHonor dikomentari | Sakelar induk mati. Unit waktu, jenis CPT, event kill tepat, persistensi dan anti-duplikasi belum dijelaskan |
| GuildSkill.ini | Enable=false; komentar meminta NPC Class 150 di GuildManager StoreList; lima nilai bonus; Experience Max=10 dan Level0-Level9 | Sakelar induk mati. Jenis level, rumus stacking, batas efek dan biaya/penyimpanan belum dijelaskan |
| Discord.ini | Enable=false; field APPLICATION_ID, image key/text dan dua button name/link | Bentuk field konsisten dengan integrasi presence/tampilan Discord, bukan bukti bot chat atau webhook. Nilai integrasi tidak dipublikasikan |
| HardwareBlocked.ini | Komentar auto reload; Num dan entri HWID berindeks | Ada konfigurasi blok perangkat; pembentukan HWID, cakupan blok dan aturan pembanding belum diketahui. Identitas perangkat tidak dipublikasikan |

Enable=false di file menunjukkan konfigurasi yang diunggah, bukan hasil observasi runtime: bisa ada konfigurasi lain, cache, atau aturan lisensi. Tidak ada fitur yang diaktifkan oleh pemeriksaan ini.

## Dungeon: spesifikasi parsial

Satu flag induk dan daftar interval bernomor. Komentar menyebut waktu valid minimum 00:01 dan maksimum 23:59. Sebelum implementasi, tentukan zona waktu server, batas inklusif/eksklusif, penanganan interval tumpang tindih dan lintas hari, perilaku ketika jadwal ditutup, serta perubahan konfigurasi secara atomik. Jangan menganggap feature ini otomatis sama dengan batas waktu di dalam dungeon.

## Guild Skill: nilai yang tersedia

| Parameter | Nilai per level dalam file |
| --- | ---: |
| ATTACK_EVERY_LV | 0.015 |
| DEFENSE_EVERY_LV | 0.015 |
| HPFP_EVERY_LV | 0.02 |
| DROPRATE_EVERY_LV | 0.05 |
| SPEED_EVERY_LV | 0.5 |

Jika pecahan dipakai sebagai rasio, 0.015 setara 1.5%; tetapi kode belum membuktikan formula maupun stacking. Khusus SPEED, jangan menganggap 0.5 berarti 50%: satuannya tidak tertulis.

Experience Max=10. Level0-Level9 berisi 1000, 2000, ..., 10000. Belum diketahui apakah ini biaya setiap kenaikan atau ambang kumulatif. Kebutuhan NPC Class 150 menunjukkan ada konfigurasi toko/NPC terkait; bukan bukti perubahan tersebut sudah terpasang.

## Enchant: pemeriksaan tabel

- ItemSave, ItemDestroy dan ItemDowngrade masing-masing memiliki 11 baris grade 0-10.
- Setiap baris berisi tepat 7 nilai, sesuai komentar urutan +1 sampai +7.
- Total 231 nilai numerik terbaca.
- Rentang ItemSave: 0-1000; ItemDestroy: 0-9999; ItemDowngrade: 0-9500.
- Pada grade 8, kolom +5, jumlah nilai tiga tabel adalah 19619. Karena itu tidak ada dasar memperlakukan ketiganya sebagai distribusi hasil eksklusif dengan skala 10000.
- Jumlah tersebut tidak otomatis berarti konfigurasi salah: tabel bisa diperiksa bertahap, bersyarat, memakai roll berbeda atau skala lain. Implementasi sebenarnya belum diketahui.
- AutoSetMaterials menurut komentar berkaitan dengan penempatan material pada board; tidak membuktikan material tidak dikonsumsi.
- File Enchant.ini belum membuktikan aturan modul Enchant Protector, penggunaan item protector atau jaminan anti-hancur.

## Cakupan terhadap 19 komponen

Bukti spesifikasi bertambah untuk Dungeon Time, Guild Point dan Guild Skill. Enchant memberi konteks upgrade umum, belum spesifikasi Enchant Protector. Looting Magnet tidak termasuk delapan file yang diterima. Potion Kill, Tower License, Infinite Potion, Player Inspector, Asset Encrypt, Broadcast Message, War Battle, Player Aura, VIP Login, Auction Cash, AutoMine Manager, Transfer Limit dan Season Pass belum dipetakan dari kumpulan ini.

## Status dan kelanjutan

Ini spesifikasi parsial berbasis konfigurasi produk referensi, bukan kode modul proyek. Tidak ada perubahan status menjadi implemented atau integration_tested. Selanjutnya lengkapi aturan yang ambigu dan identifikasi source/SDK atau antarmuka server yang terbukti. Hasil fungsi gameplay tidak dapat diperoleh hanya dengan membuat ulang file INI.

Bahan lanjutan paling relevan: Looting_Magnet.ini dan dokumentasi perilaku fitur prioritas, serta keberadaan source/SDK atau baseline pengembangan. Jangan mengirim Main.ini asli, lisensi, kredensial atau data pemain untuk tahap pemetaan ini.
