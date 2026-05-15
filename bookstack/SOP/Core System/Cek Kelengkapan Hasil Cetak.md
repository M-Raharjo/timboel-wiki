---
bookstack_type: page
bookstack_id: 563
name: Cek Kelengkapan Hasil Cetak
slug: cek-kelengkapan-hasil-cetak
book_id: 37
chapter_id: null
created_at: '2026-04-24T01:53:47.000000Z'
updated_at: '2026-04-24T03:29:16.000000Z'
source_url: null
---

**Tujuan:**  
Untuk mengecek kelengkapan hasil cetak 3d print proyek

**Trigger:**  
Komponen rangkai proyek sudah dibagi ke dalam kelas per 10 komponen 

**Input:**  
- Dzokumen fisik Checklist Komponen Rangkai proyek yang tengah dikerjakan
- Bolpen
- Spidol hitam
- Akses ke [folder gdrive 3D print proyek](https://drive.google.com/drive/folders/1eSAQJrRWF6qD_M45ju9KKmKAiFJgmxj6)
- Software Babylon Sandbox [Babylonjs](https://sandbox.babylonjs.com/)

**Langkah:**  
1. Pilih satu kelas komponen untuk diperiksa (contoh kelas 001-010, kelas 100-110), cek kode komponen dari masing-masing komponen
2. Cocokan kode komponen tersebut ke dokumen checklist komponen rangkai, hitamkan menggunakan spidol kode angka yang ditemukan.
3. Lakukan untuk semua kelas di proyek ini
5. Buka folder gdrive 3d print proyek. Buka sub folder `nama proyek - main body cut`. Contoh: [![](https://wiki.pttimboel.com/uploads/images/gallery/2026-04/scaled-1680-/bY8tRZCispZIher4-image-1776997416446.png)](https://wiki.pttimboel.com/uploads/images/gallery/2026-04/bY8tRZCispZIher4-image-1776997416446.png)
6. Pilih satu angka di checklist komponen rangkai proyek yang tidak dihitamkan, cari kode komponen di folder gdrive yang memiliki angka tersebut.
7. Apabila kode komponennya memiliki label `tiny`, silang angka itu pada checklist komponen rangkai. Jika tidak, lingkari.
8. Ulangi langkah 6 sampai tidak ada angka di dokumen checklist komponen rangkai yang perlu disilang lagi.
9. Download dari google drive `nama proyek - main body cut` file  dengan kode komponen yang belum diberi tanda/coretan/blok spidol
10. Buka program atau website babylon.js sandbox.
11. Pilih satu file 3D yang akan diperiksa, Buka babylon -> Layar kanan bawah -> klik logo upload (panah ke atas) untuk upload file 3d yang didownload. Contoh visual: [![](https://wiki.pttimboel.com/uploads/images/gallery/2026-04/scaled-1680-/uJ68Dr3fyUuRqzdB-image-1776998105912.png)](https://wiki.pttimboel.com/uploads/images/gallery/2026-04/uJ68Dr3fyUuRqzdB-image-1776998105912.png)
12. Cocokkan file yang dibuka dengan komponen yang tidak memiliki kode komponen.
13. Apabila bentuknya sesuai, tulis kode komponen file di permukaan komponen menggunakan spidol (contoh kode: AER-010)
14. Hitamkan angka dari kode komponen yang ditulis pada komponen di checklist komponen rangkai
16. Ulangi langkah 11 sampai semua komponen tanpa kode sudah teridentifikasi atau menyisakan komponen yang gagal teridentifikasi

**Output:**  
Dokumen fisik checklist komponen rangkai selesai dikerjakan, komponen 3d telah dicek kelengkapannya