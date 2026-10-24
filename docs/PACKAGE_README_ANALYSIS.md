# Analisis ReadMe paket OWN PROTECTION

Tanggal pemeriksaan: 24 Oktober 2026. Sumber: ReadMe.txt yang diberikan pengguna dari folder server. Isi tidak diperlakukan sebagai instruksi untuk menjalankan software atau mengubah database.

## Temuan terverifikasi dari teks

- Nama executable ZoneServer tidak boleh diubah menurut paket ini.
- Instalasi menyebut tiga komponen: SnooperGS.exe, SnooperGS.dll dan folder PROTECT.
- IP publik dikonfigurasi melalui PROTECT/Main.ini.
- Mode tanpa License.dat disebut memiliki batas 20 login; mode berbayar menggunakan License.dat dari pengembang.
- Dokumen menyebut NPCLinkItem serta SqlAddon BILLING, NEW_FIX_2022 dan POTION_SAVE.
- Rincian konfigurasi lainnya dirujuk ke komunitas Discord.

Ketentuan 20 login adalah klaim ReadMe produk referensi, belum diuji pada file pengguna. Tidak ada pengubahan atau bypass lisensi dalam proyek ini.

## Hubungan dengan bukti sebelumnya

| Bukti | Arti yang dapat disimpulkan | Batas |
| --- | --- | --- |
| ReadMe menyebut SnooperGS.exe + SnooperGS.dll | Paket tersebut mengarahkan instalasi melalui komponen SnooperGS | Arsitektur, ABI, urutan pemanggilan dan versi belum diperiksa |
| Screenshot RF_Bin menunjukkan SnooperGS, SnooperGS.dll, ODZone dan ODGuard.dll | Ada dua set nama komponen dalam satu folder | Tidak membuktikan set mana yang aktif atau bahwa keduanya dapat digabung |
| ODZone.exe yang diunggah mengimpor ODGuard.dll | Dependensi langsung executable tersebut telah terbukti melalui PE | Tidak membuktikan ODZone adalah executable yang dimaksud ReadMe SnooperGS |
| ReadMe menyebut eksekusi SQL addon manual | Paket mempunyai petunjuk instalasi manual | Isi skrip belum tersedia; belum dapat dinilai aman/kompatibel |
| PDF Database menjelaskan migrasi otomatis dan SqlAddon terpisah | Dokumentasi lain memakai mekanisme migrasi yang lebih terstruktur | Versi/build yang tepat dari kedua dokumen belum diketahui |

ReadMe dan PDF Database mempunyai instruksi SQL yang berbeda. Jangan menggabungkan kedua prosedur begitu saja. Ini indikasi perbedaan paket/petunjuk; tidak cukup untuk menentukan kronologi atau versi rilis secara pasti.

## Keputusan teknis

1. Jangan rename ODZone menjadi SnooperGS berdasarkan kemiripan ukuran atau nama.
2. Jangan menjalankan SQL addon atau migrasi sebelum mencocokkan build dan meninjau isi skrip pada salinan database.
3. Jangan menyimpulkan paket ini sudah menyediakan seluruh 19 komponen pilihan; ReadMe tidak mencantumkan spesifikasi tersebut.
4. Tidak ada patch gameplay siap distribusi, titik hook, format paket atau migrasi proyek yang telah diverifikasi.
5. Perlu identifikasi SnooperGS.exe dan SnooperGS.dll untuk memahami paket yang dimaksud ReadMe sebelum memilih baseline integrasi.

## Bahan berikutnya yang diprioritaskan

Kirim SnooperGS.exe dan SnooperGS.dll dari folder RF_Bin untuk analisis statis; jangan menjalankannya sebagai bagian pengumpulan bahan. Jika dibutuhkan selanjutnya, isi skrip SqlAddon dan ReadMe NPCLinkItem dapat ditinjau secara terpisah.

PROTECT/Main.ini, License.dat, password, dump database dan data pemain tidak diperlukan untuk pemeriksaan header/dependensi. Source/SDK dan executable client yang cocok tetap dibutuhkan untuk memastikan cakupan pengembangan. Komponen pihak ketiga tidak disalin menjadi implementasi modul proyek.
