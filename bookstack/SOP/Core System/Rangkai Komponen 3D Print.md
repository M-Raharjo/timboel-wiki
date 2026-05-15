---
bookstack_type: page
bookstack_id: 564
name: Rangkai Komponen 3D Print
slug: rangkai-komponen-3d-print
book_id: 37
chapter_id: null
created_at: '2026-04-24T03:38:54.000000Z'
updated_at: '2026-04-24T06:16:51.000000Z'
source_url: null
---

**Tujuan:**  
Merangkai komponen 3D Print menggunakan panduan rangkai

**Aturan**
- Assembly sequence dikerjakan urut dari atas ke bawah
- Sambungan komponen hanya menggunakan Lem G.

**Trigger:**  
Komponen selesai di cek kelengkapannya dan siap dirangkai

**Input:**  
- Komponen rangkai 3d print proyek
- Dokumen fisik Checklist komponen rangkai
- Dokumen fisik assembly sequence komponen proyek
- cutter 2 pcs
- Lem G 10 pcs
- Lakban kertas 1 pcs
- dokumen fisik foto persepektif 3 sudut proyek

**Langkah:**  
1. Persiapkan dokumen assembly sequence dari parsel rangkai. Contoh:[![](https://wiki.pttimboel.com/uploads/images/gallery/2026-04/scaled-1680-/V9TeykaWmxwcnG8N-image-1777010400385.png)](https://wiki.pttimboel.com/uploads/images/gallery/2026-04/V9TeykaWmxwcnG8N-image-1777010400385.png)
2. Baca satu perintah pasang dokumen assembly sequence. Contoh: `(3) + (4)`
3. Cari komponen dengan nomor komponen yang tertulis di perintah pasang (Contoh: `AER-003` adalah komponen `3` di dokumen assembly sequence)
4. Apabila komponen tidak ditemukan, cek nomor komponen di dokumen checklist komponen rangkai. Apabila nomornya disilang, hiraukan komponen tersebut dan silang angkanya di assembly sequence.
5. Gabungkan kedua komponen tersebut.
6. Alirkan Lem G di celah sambungan antar kedua komponen tersebut. Tunggu sampai kering dan komponen tidak mudah lepas
7. Taruh komponen di kelas sesuai dengan angka paling kecil gabungan komponen. Contoh: komponen (3) + (14) + (20), hasilnya ditaruh di kelas 1-10 karena angka paling kecil adalah (3)
8. Centang perintah pasang dokumen assembly sequence untuk menandakan kalau perintah selesai dilaksanakan
9. Ulangi dari langkah 2 sampai semua perintah pasang assembly sequence selesai dikerjakan

**Output:**  
Komponen rangkai selesai disatukan menjadi barang proyek 3D