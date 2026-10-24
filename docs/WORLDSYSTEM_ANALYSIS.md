# WorldSystem dan ItemConsume: analisis kapasitas dan startup

Tanggal: 24 Oktober 2026. Sumber: WorldSystem.ini, WorldSystem.bin dan ItemConsume.ini yang diunggah pengguna, ditambah ODZone.exe dan SnooperGS.exe yang diperiksa sebelumnya. Semua file asli tetap utuh. Tidak ada server, SQL atau patch yang dijalankan.

## 1. Temuan utama kapasitas

WorldSystem.ini berisi:

```ini
[System]
AccountAddress = 127.0.0.1
LimUserNum = 1337
```

Ini nilai pada file yang diunggah, bukan bukti jumlah pemain yang saat ini aktif atau konfigurasi yang benar-benar dibaca server berjalan.

Analisis statis menelusuri string LimUserNum ke pemanggilan GetPrivateProfileIntA. Pada preferred VA 0x1401f7776 sampai 0x1401f77c8:
- R9 menunjuk .\\Initialize\\WorldSystem.ini.
- R8D berisi 0x9e4, yaitu 2532, sebagai nilai default.
- RDX menunjuk LimUserNum.
- RCX menunjuk System.
- Call melalui IAT 0x184aef1f8 terpetakan ke KERNEL32.dll / GetPrivateProfileIntA.
- Nilai kembalian disimpan pada field object +0x38476924.
- Kode membandingkan field tersebut dengan 0x9e4 dan menulis 0x9e4 jika nilainya lebih besar.

Ini membuktikan loader konfigurasi native memakai default 2532 dan clamp atas 2532. Belum ada penelusuran penuh semua pemakaian field, alokasi pool, lisensi guard, Account Server atau protokol client.

Rentang byte kode ini identik pada SnooperGS.exe yang diunggah. VA berlaku pada preferred image mapping; ini bukan instruksi menulis memori atau alamat patch.

## 2. Implikasi untuk target 2532 pemain

Perubahan konfigurasi yang relevan untuk diuji adalah mengubah nilai LimUserNum pada bagian System dari 1337 menjadi 2532 dalam salinan uji. Tidak ada kebutuhan yang terbukti untuk mengubah immediate 0x9e4 pada binary untuk target ini: loader native yang diperiksa sudah memiliki batas tersebut.

Ini BUKAN klaim server sudah mendukung 2532 pemain stabil. Batas guard/lisensi bisa lebih rendah; pool indeks, proses akun, socket, database dan kinerja perlu pengujian. ReadMe menyebut mode tanpa License.dat dibatasi 20 login. Tidak ada perubahan lisensi atau upaya melewati batas tersebut dalam studi ini.

Screenshot/file konfigurasi bukan bukti runtime. Catat startup log dan konfigurasi efektif, uji login bertahap serta rollback sebelum perubahan produksi.

## 3. Pengaturan lain WorldSystem.ini

| Bagian | Nilai teramati | Interpretasi terbatas |
| --- | --- | --- |
| System / AccountAddress | 127.0.0.1 | Alamat loopback; bila field dipakai sebagaimana namanya, proses akun diharapkan pada host yang sama. Port/proses tepat belum diketahui |
| MainThread | SleepTerm=4000, SleepValue=1, SleepIgnore=0 | Parameter timing; satuan dan dampak performa belum ditelusuri, jangan ubah sebagai optimasi tanpa pengukuran |
| Messenger | Use=TRUE | Flag messenger aktif pada file |
| RankJob | JobHour=23, JobMin=40 | Parameter penjadwalan, bukan bukti zona waktu atau hasil eksekusi |
| Rule | AttackSpareDelay=200 | Parameter terkait aturan attack; satuan/algoritme belum dipastikan |
| Economy | Default_MgrVal, Default_TaxVal, Default_OreVal dan key tanggal lama | Nilai ekonomi, penerapan dan unit perlu kode/dokumen |
| HolySystem | Keeper, StoneNum=3, tiga set stone map/dummy/monster/race | Konfigurasi entitas HolySystem; bukan bukti spawn berhasil |
| Buddha Event / CLASS REFINE EVENT / PcBang Favor | Flag FALSE | Fitur tersebut dinonaktifkan di file |
| Time Limit | Use=FALSE; tiga pasangan Time/Percent dan parameter logout/notify | Tidak aktif; jangan disamakan dengan kapasitas concurrent player atau jadwal Dungeon_Timer |
| VersionCheck | Hanya komentar, tidak ada Ver_CheckKey aktif | Tidak membuktikan pemeriksaan versi client dimatikan atau konfigurasi lengkap |

Komentar VersionCheck menyebut sinkronisasi key dengan binary client. Format dan nilai tidak tersedia. Tidak ada alasan untuk menambahkan key tebakan atau menonaktifkan validasi.

## 4. ItemConsume.ini

```ini
[AWAY_PARTY]
ItemConsume = true
ItemCode = ircht01
MoneyConsume = false
Money = 55000

[AllRaceChat]
ItemConsume = true
ItemCode = ircht01
MoneyConsume = true
Money = 10000
```

Makna berdasarkan nama field:
- AWAY_PARTY mengonfigurasi konsumsi item ircht01 dan flag konsumsi uang false. Nilai uang 55000 tetap tertulis, tetapi tidak boleh dianggap terpotong ketika flag false tanpa pembuktian runtime.
- AllRaceChat mengonfigurasi konsumsi item ircht01 serta uang 10000, dengan kedua flag true.
- Jangan menebak item ircht01 adalah potion atau menentukan nama item tanpa tabel item.
- Ini bukan bukti implementasi Infinite Potion, Potion Kill, atau Broadcast Message administratif.

String .\\Initialize\\ItemConsume.ini, AWAY_PARTY dan AllRaceChat ditemukan pada ODZone di sekitar penanda CMainThread::LoadWorldSystemINI(). Ini memperkuat hubungan konfigurasi dengan executable; semantik pemotongan transaksi belum ditelusuri.

## 5. WorldSystem.bin

- Ukuran 320 byte.
- Tidak mempunyai header executable MZ; bukan EXE yang dijalankan.
- Tidak terlihat sebagai INI teks biasa; belum diketahui formatnya.
- ODZone mengandung string .\\Initialize\\WorldSystem.bin (offset file 0x76bedd), berdekatan dengan pesan CCryptor::Instance()->Init() Fail.
- Kedekatan string memberi petunjuk hubungan dengan inisialisasi cryptor, bukan bukti algoritme, isi plaintext, tujuan lisensi atau mekanisme verifikasi.
- Tidak dilakukan dekripsi atau pengubahan byte. Jangan menyamakan .bin ini dengan file client RF_Online.bin.

## 6. Identitas file

| File | Byte | SHA-256 |
| --- | ---: | --- |
| WorldSystem.ini | 1433 | a2714d22ea79acec5134900640c93d27e1af11ea9069cdd1cb5b9d32120a85a7 |
| ItemConsume.ini | 186 | 7c309ba8de86c1e5bafb9c316ded53f0efe946d62f7d46c805999463e9fb38cf |
| WorldSystem.bin | 320 | 4320307438453fdab0b3fbbfd9a126fd67edbe9b943ce66847d89aeb9e198821 |

## 7. Bukti yang masih diperlukan

Konfigurasi efektif saat startup, kondisi lisensi yang berlaku, keberhasilan baseline login, source/SDK atau penelusuran pemakaian field kapasitas, dan hasil uji beban pada target. Tidak ada file patch kapasitas atau fitur gameplay yang dirilis dari analisis ini.
