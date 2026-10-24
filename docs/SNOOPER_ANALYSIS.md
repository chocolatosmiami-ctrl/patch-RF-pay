# Pemeriksaan SnooperGS EXE dan DLL

Tanggal: 24 Oktober 2026. Sumber: dua file yang diunggah pengguna di chat. Pemeriksaan hanya statis dengan file, SHA-256, objdump, dan pembacaan PE menggunakan Python. Tidak ada target yang dijalankan, dimodifikasi, di-unpack, atau dihubungkan ke database. REA MCP laptop tidak tersedia di sesi ini.

## Identitas terverifikasi

| File | Ukuran byte | Format | Machine |
| --- | ---: | --- | --- |
| SnooperGS.exe | 10457088 | PE32+ GUI | 0x8664 / x64 |
| SnooperGS.dll | 12644352 | PE32+ DLL | 0x8664 / x64 |

SHA-256:

- EXE: d5e1b8825129783442b48497da035c9284d4ffc0be70404b67b37317304c61e6
- DLL: 8226c9f9d91891fef62085fc195f5f2fee70293de83fb38883b066e5756ac8b5

## Hubungan executable dan DLL

EXE mengimpor SnooperGS.dll melalui ordinal 1. DLL menyediakan satu export; parsing tabel nama menunjukkan __Snooper. Ordinal base adalah 1 dan Export Address Table berisi satu entri. Ini membuktikan kecocokan arsitektur dan tersedianya ordinal yang diminta; bukan bukti ABI, urutan startup, atau kompatibilitas runtime lengkap. objdump memperingatkan nama export tidak dapat ditampilkan melalui parsernya; nama diperoleh dari pemetaan RVA tabel PE langsung.

Nama DLL pada EXE berada di offset file 0x9f8fcc. Section EXE adalah .text, .rdata, .data, .pdata, .idata, .didat, .rsrc dan .NewIT. Entry-point RVA 0x4dd320.

Dependensi EXE yang terlihat juga mencakup ODBC32.dll, WS2_32.dll, AntiCpSvr.dll, RFACC.dll, d3dx9_30.dll, MSVCP80D.dll, MFC80D.DLL dan MSVCR80D.dll. Belum diverifikasi bahwa seluruh dependensi tersedia dan berarsitektur sesuai pada mesin pengguna.

## Perbandingan dengan ODZone.exe

Dibandingkan dengan ODZone.exe pada commit d67e0b6e47e87c67403118bc292a38d45a85ffc0:

- Ukuran file sama persis.
- Byte-by-byte menunjukkan hanya satu rentang berbeda, sepanjang 13 byte: offset 0x9f8fcc sampai sebelum 0x9f8fd9.
- Rentang itu adalah area nama dependensi ODGuard.dll versus SnooperGS.dll; area lainnya identik.

Kesimpulan terbatas: kedua executable menggunakan byte dasar yang sama di luar perubahan rentang tersebut. Ini memperjelas hubungan paket ODGuard dan SnooperGS. Tidak membuktikan DLL keduanya mempunyai fitur yang sama, dapat dipertukarkan, atau sah dijalankan dengan mengganti nama file. Jangan membuat patch pengganti hanya dari kemiripan executable ini.

## DLL dan batas observasi

- 12 section; beberapa bernama spasi, dengan .rsrc, .edata, .idata, .tls dan .winlice.
- Ditemukan string ASCII WinLicense pada offset 0x12f27e.
- Ditemukan string UTF-16LE License.dat pada offset 0x595aeb.
- Gabungan penanda .winlice dan WinLicense konsisten dengan penggunaan pelindung WinLicense; belum ada pembongkaran atau verifikasi runtime mekanisme tersebut.
- Impor statis yang terlihat: kernel32.dll, USER32.dll, GDI32.dll, ADVAPI32.dll, ODBC32.dll, WINMM.dll, Normaliz.dll, WLDAP32.dll, CRYPT32.dll dan WS2_32.dll.
- Daftar impor yang terlihat tidak menjamin seluruh dependensi runtime telah terungkap.
- Nama export dan penanda lisensi tidak mengungkap parameter fungsi, struktur objek, format paket, atau rincian modul.

## Status pengembangan

ReadMe yang menyebut pasangan SnooperGS.exe dan SnooperGS.dll sekarang didukung oleh bukti import EXE dan export DLL. Masih belum ada bukti bahwa semua fitur pilihan tersedia pada versi ini; tidak ada modul gameplay proyek yang selesai atau diuji.

Bahan yang paling berguna selanjutnya adalah spesifikasi perilaku modul dan source/SDK atau baseline pengembangan yang tersedia. Untuk pemetaan konfigurasi tanpa data rahasia, cukup mulai dengan daftar nama file di PROTECT/Configs. Tidak diperlukan Main.ini asli, License.dat, kredensial, atau dump data pemain. Client yang cocok serta pengujian baseline login tetap belum tersedia.

Binary pihak ketiga yang dikirim di chat tidak dipublikasikan ke repository oleh pemeriksaan ini. Laporan hanya menyimpan metadata dan kesimpulan teknis.
