---
bookstack_type: page
bookstack_id: 558
name: Mencetak Komponen Proyek 3D print
slug: mencetak-komponen-proyek-3d-print
book_id: 37
chapter_id: null
created_at: '2026-04-22T20:04:33.000000Z'
updated_at: '2026-05-01T17:22:05.000000Z'
source_url: null
---

**Tujuan:**  
Mencetak komponen proyek 3d print menggunakan file plate


**Trigger:**  
Perintah cetak proyek 3d print diberikan

**Input:**  
- File plate proyek print
- Dokumen checklist komponen print berisi data proyek print dan daftar plate yang akan dicetak. Contoh: [![](https://wiki.pttimboel.com/uploads/images/gallery/2026-04/scaled-1680-/YJA7rTCYewEcL8v4-image-1777432716322.png)](https://wiki.pttimboel.com/uploads/images/gallery/2026-04/YJA7rTCYewEcL8v4-image-1777432716322.png)

**Langkah:**  
1. Cek dokumen checklist komponen print untuk nama proyek print.
2. Lakukan proses [Buka File Plate](https://wiki.pttimboel.com/books/core-system/page/membuka-file-plate-proyek-3d-print) untuk nama proyek terkait.
3. Lakukan prosedur [Cek Proses Kerja Printer](https://wiki.pttimboel.com/books/core-system/page/mengecek-proses-kerja-printer) untuk menyiapkan/mengosongkan printer.
4. Cek dokumen checklist komponen print, pilih satu baris Plate yang kolom printernya kosong. Contoh: Baris Plate `1`, kolom Printer-nya kosong. Pilih plate 1 untuk diproses

[![](https://wiki.pttimboel.com/uploads/images/gallery/2026-04/scaled-1680-/YJA7rTCYewEcL8v4-image-1777432716322.png)](https://wiki.pttimboel.com/uploads/images/gallery/2026-04/YJA7rTCYewEcL8v4-image-1777432716322.png)

5. Buka Bambu Studio yang membuka file plate proyek
6. Layar bagian atas: Klik opsi preview
7. Layar bagian tengah, kolom berisi gambar tampilan kecil komponen: klik plate dengan nomor yang sama dengan yang dipilih di langkah 4
8. Layar pojok atas kanan: klik tanda panah ke bawah, pilih opsi `print plate`. Klik `print plate` lagi.
9. Klik opsi Printer (klik di gambar printernya) -> pilih printer yang tidak aktif bekerja (pastikan tidak muncul peringatan error)

Contoh peringatan error:
[![](https://wiki.pttimboel.com/uploads/images/gallery/2026-05/scaled-1680-/AoRuGidwQgYg5Yb3-image-1777655639356.png)](https://wiki.pttimboel.com/uploads/images/gallery/2026-05/AoRuGidwQgYg5Yb3-image-1777655639356.png)

10. Klik opsi Filament -> Pilih opsi AMS apabila tersedia (pilih opsi A1, A2, A3, atau A4 yang tersedia). Jika tidak ada opsi AMS, pilih EXT

Contoh peringatan error: [![](https://wiki.pttimboel.com/uploads/images/gallery/2026-05/scaled-1680-/V95TRJlmZDYUAtSe-image-1777655690296.png)](https://wiki.pttimboel.com/uploads/images/gallery/2026-05/V95TRJlmZDYUAtSe-image-1777655690296.png)

11. Klik Send. Tulis nama printer di baris Plate yang dicetak. Contoh: setelah mencetak komponen Plate 1 di printer Unagi, tulis Unagi di baris `plate` 1, kolom `printer` pada dokumen checklist komponen print.
12. Tunggu hingga Bambu Studio selesai mengirim file ke printer (jendela proses kirim plate ke printer tutup otomatis).

Contoh opsi printer UNAGI dan filament AMS (A1) yang tidak error, dan situasi Bambu Studio sedang proses kirim file ke printer:
[![](https://wiki.pttimboel.com/uploads/images/gallery/2026-05/scaled-1680-/RbpeSP4MnutYdrCz-image-1777655885928.png)](https://wiki.pttimboel.com/uploads/images/gallery/2026-05/RbpeSP4MnutYdrCz-image-1777655885928.png)

13. Jika sudah selesai kirim, ulangi mulai dari langkah 5 hingga semua printer terisi/bekerja/opsi memilih printer menunjukan error.

**Output:**  
Printer mencetak komponen sesuai dengan dokumen checklist komponen print