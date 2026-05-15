---
bookstack_type: page
bookstack_id: 417
name: SOP 3D Printing
slug: sop-3d-printing
book_id: 33
chapter_id: null
created_at: '2026-02-06T13:13:01.000000Z'
updated_at: '2026-04-16T06:35:47.000000Z'
source_url: null
---

Notes
- tiap fase dikasih siapa yang garap, konek ke siapa
- kasih contoh gambar untuk mempermudah penggunaan aplikasi. Kasih arah kemana harus lihat juga lebih baik
- Semua yang perlu diklik, ditulis untuk



## Link Penting
- Link Monitor Pekerjaan 3D: [Monitor Lizard](https://docs.google.com/spreadsheets/d/1fsVSR_fHL2AxGm0g35uOucx71AizGN1MJaRNfw7o-mY/edit?gid=610922543#gid=610922543)
- Link Google Drive Penyimpanan File Kerja 3D Printing: [Operasional 3D Printing](https://drive.google.com/drive/folders/1eSAQJrRWF6qD_M45ju9KKmKAiFJgmxj6)

## Nomor Penting
- Egi (Staff 3D) +62 857-1581-0367
- Naufan (Assisten Produksi) +62 858-0283-7291
---

## Struktur SOP

1. Alur Kerja 3D Printing
2. Alur Operasional 3D Printing
3. Arsip & Manajemen Data
4. Prosedur Tambahan

---

## Aplikasi yang Digunakan

* Blender
* Instant Meshes
* Autodesk Meshmixer
* LuBAN
* Bambu Studio
* Google Drive

PT Timboel menggunakan komputer di meja staff 3d Printing sebagai pusat kontrol utama operasi.
Proses printing berbasis SD Card dan checklist fisik.

---
## Istilah
- **NamaProyek**
  - NamaProyek digunakan untuk identifikasi proyek yang dikerjakan
  - Menggunakan nama/julukan produk sebagai pembeda
    - Verduma, Toroso, Ten Thousand Strands, Spiritus Alatus
- **Cut**
  - File dengan label "Cut" pada namanya adalah file yang siap masuk proses Slicing dan Printing
- **Kode Komponen**
  - Singkatan 3 huruf dari nama barang. Untuk mempermudah transfer barang dari printer menuju ke boks komponen dan memeriksa kelengkapan komponen.

---

## 1. Alur Kerja 3D Printing

### 1.1 Folder Penyimpanan

* Buat folder penyimpanan untuk barang yang akan dikerjakan di Google Drive Penyimpanan File Kerja 3D Printing
  * Gunakan folder sampel sebagai contoh folder
>**FILE HASIL PROSES KERJA 3D PRINTING DI-UPLOAD KE FOLDER TERSEBUT MENGIKUTI ATURAN BAB 3 - ARSIP DAN MANAJEMEN DATA**

### 1.1 Sumber Model 3D

* Hasil scan
* Website model 3D
* Vendor / 3D modeller

Beri nama `NamaProyek - File3d`, ekstensi `.stl`, upload ke dalam folder penyimpanan.

---

### 1.2 Persiapan Model
<details>

  <summary>Blender — Cleaning & Sizing </summary>
* Import model 3D (NamaProyek - File3d)
* Bersihkan:

  * Non-manifold geometry
  * Lubang besar
  * Objek scan yang tidak diperlukan
* Set ukuran model ke ukuran akhir produk
* Pastikan model solid berisi, tidak hollow/kopong
* Export dengan ekstensi `.obj`

</details>

---

### 1.3 Retopologi & Validasi Mesh
<details>

<summary>Instant Meshes — Retopology</summary>

* Import file hasil cleaning & sizing
* Atur **Target Vertex Count** sesuai kebutuhan finishing

  * Catatan: semakin tinggi → detail dan kehalusan permukaan makin bagus, beban proses komputer makin tinggi
* Klik **Solve** (Orientation & Position Field)
* Export `.obj`

</details>

<details>
<summary>Blender — Mesh Validation</summary>

* Import file hasil retopologi
* Cek:

  * Penampakan siluet halus, tidak berkarang/jaggy
  * Kepadatan mesh merata
* Jika hasil buruk → ulangi tahap Retopologi

</details>
<details>
<summary>Blender - Base Preparation</summary>
  
* Extrude sisi bawah model
* Potong bagian bawah menggunakan metode Boolean
* Export `.obj`

</details>
---

### 1.4 Shelling

<details>
  <summary>Autodesk Meshmixer — Hollow</summary>

* Import file hasil validasi mesh
* Edit → Hollow
* Offset Distance: **4 mm**
* Jika muncul lubang:

  * Atur Solid Accuracy & Mesh Density
  * Kecilkan Hole Radius bila perlu
* Export `.obj`

  * Format nama: `NamaProyek - Model3D`, upload ke folder penyimpanan, subfolder Model3D
</details>
---

### 1.5 Pemotongan Model

<details>
<summary>Blender — High Priority Cut</summary>

* Import file hasil shelling
* Identifikasi **High Priority Surface**

  * Contoh: wajah patung, ornamen utama, bagian yang menjadi fokus pandangan konsumen saat meliaht patung
* Potong bagian high priority menggunakan metode boolean
* Potong komponen agar masuk ke dalam ukuran print dibawah 230x230x230 cm
* Export:

  * `NamaProyek - Nama Komponen - HIGH PRIORITY CUT.stl` untuk potongan high priority, upload ke folder penyimpanan, subfolder High Priority
  * `NamaProyek - File untuk LUBAN.stl` untuk potongan sisanya, upload ke folder penyimpanan
</details>
---

### 1.6 Modular Cutting

**LuBAN — Modular Cut**

* Import file `NamaProyek - File untuk LUBAN.stl`
* Mesh → Cut

**Pengaturan Utama**

* Method: Modular Cut
* Unit: mm
* Pastikan ukuran model sesuai ukuran akhir

**3D Printer**

* Bed Shape: Rectangle
* Printer Size: X 230 mm; Y 230 mm; Z 230 mm
* Close Cut: YES
* Axial Cut: YES
* `Part Number`: Yes

  * Start Number: 1
  * Prefix: 3 huruf inisial/singkatan nama model
    * Contoh: MIM, VER, SIR, K70

**Connector**

* Type: Plug

* Shape: Square (Number = 8)

* Tolerance: -0.2 mm

* Depth ratio: 1,5

* Klik **Cut**

* Simpan ke folder: `NamaProyek - MAIN BODY CUT`


---

### 1.7 Slicing

**Bambu Studio**

* Prepare → Add file (ctrl + I):

  * Semua file di folder `Main body Cut` dengan ekstensi .stl (hiraukan komponen berlabel `tiny`), atau
  * Semua file di folder `HIGH Priority` dengan ekstensi .stl

* Load as single object with multiple parts: **NO**

**Auto Arrange**

* Spacing: 2 mm
* Auto Rotate: ON
* Pilih Allow multiple materials on same plate

**Penataan Plate**

* Gunakan **Lay on Face**
* Minimalkan permukaan yang menggantung (overhang)
* Hindari bagian dengan sambungan plug tidak menempel lantai print
* Maksimalkan jumlah komponen per plate
* Tiap  komponen diberi label dengan `Text Shape` -> nama `part number` untuk masing-masing komponen
  * `Part Number` berisi 3 digit singkatan nama produk yang diprint dan nomor part
    * contoh singkatan: MIM, VER, SIE, K70
    * contoh part number dengan singkatan: MIM-001, VER-025, SIE-011
      * MIM-001 berarti part pertama dari model MIM (Mind in Motion)
    * >Part Number komponen High Priority diberi inisial **HP**
  * Thickness -> 1 mm
  * **Taruh Part Number di lokasi permukaan luar patung**

**Opsi Strength**
* Sparse Infill density: 5%

**Opsi Support**

* Enable Support: ON

* Type: Tree (Auto)

* Threshold Angle: 38–45°

**Slice dan Print**

* Pilih opsi Slice Plate/Slice All untuk memulai proses slicing


* Simpan project: `NamaProyek_PLATE`, upload ke Folder Penyimpanan, subfolder Plate

  * Apabila membutuhkan penyimpanan lebih dari 1 file, tulis daftar nomor komponen pada judul file
    * Contoh: `Verduma_PLATE - 001-024` dan `Verduma_Plate 025-045

### 1.8 Printing
* Siapkan boks penyimpanan komponen, tandai dengan kode Part Number komponen yang kan dicetak
* Taruh file plate di desktop komputer untuk kemudahan akses
* Import file plate ke dalam Bambu Studio.
* Cetak formulir Checklist Komponen Print, tulis judul file plate yang dicetak dan semua Plate yang akan di print ke dalam formulir
  * daftar plate merujuk pada nomor plate yang akan dicetak di dalam file plate
    * Contoh penamaan: Plate nomor 1 di dalam Bambu Studio (ditunjukan dengan angka 1 di samping visual plate) bisa disebut sebagai Plate 1, dan seterusnya.
* Pilih plate yang akan dicetak. Pilih print.
* Pilih printer yang sedang tidak bekerja (tidak busy), lalu pilih send.
* Tulis nama printer yang digunakan mencetak di samping nama plate yang sedang dicetak
* Apabila semua komponen sudah selesai dicetak, lanjut ke 

---

## 2. Alur Operasional 3D Printing

### 2.1 Persiapan Produksi

* Siapkan project dan file hasil slicing
* Buat [**Checklist Komponen Print**](https://docs.google.com/spreadsheets/d/1soNDEX7HZvYy2PJOUBJRKML9ayCND45nkkICx0ISoyY/edit?gid=0#gid=0)

**Format Judul Checklist**
`Nama Produk – Dimensi - Kode Part Number`.

**Kolom Checklist**

* Nomor Plate (Bambu Studio)
* Nama Printer
* Proses?
* Selesai?

---

### 2.2 Proses Print
**Kebutuhan Print**
* Lembar Checklist Komponen print
* Alat tulis (bolpen dan spidol)
* Mesin Printer Bambu Lab
* Box komponen dengan label (lakban kertas) berisi info Kode Komponen (3 huruf)
* Sticky note ukuran 4x10 cm

<details>
<summary>Alur Print Lewat Printer</summary>
  
1. Cek printer
  - Printer masih proses: langsung ke langkah 8
  - Printer selesai proses/kosong: lanjut ke langkah 2

2. Keluarkan komponen dari printer, hitamkan kode komponen menggunakan spidol, masukan ke box sesuai part number komponennya
3. cek nama printer di checklist yang belum dicentang kolom "Selesai?"-nya, centang kolom "Selesai?".
4. Aktifkan kontroler bambu lab menggunakan tombol arah. Pilih simbol folder (paling bawah), lalu pencet ok. Cek file di dalam
  - Tidak ada file dengan nama "Plate": tempelkan sticky note ke printer, tulis "FILE HABIS"

5. Cek nama file plate di dalam checklist
  - Kolom "Printer" sudah diisi: cek file selanjutnya
  - Kolom "Printer" belum diisi: cetak file tersebut dengan pencet tombol OK dua kali

6. Isi kolom printer dengan nama printer yang mencetak file tersebut
7. Cek apakah printer berhasil mencetak lapisan pertama di atas plate (ada hasil cetakan yang menempel di papan printer
  - Apabila gagal, tempel sticky note ke printer, tulis "gagal cetak"
  - Apabila berhasil, printer berhasil menjalankan proses, abaikan
    
8. Ulangi langkah 1 untuk printer lainnya. Apabila semua printer sedang mencetak/ditandai sticky notes, shift selesai.
</details>

<details>
<summary>Alur Print Bambu Studio</summary>

1. Cek Printer
  - Printer masih proses: langsung ke langkah 8
  - Printer selesai proses/kosong: lanjut ke langkah 2

2. Keluarkan komponen dari printer, hitamkan kode komponen menggunakan spidol, masukan ke box sesuai dengan part number komponennya
3. Cari nama printer itu di checklist. Centang kolom "Selesai?" yang belum dicentang.
4. Buka file `NamaProyek_PLATE` sesuai dengan checklist.
5. Cari nama plate di checklist yang belum punya printer.
6. Cari plate tersebut di Bambu Studio, pilih opsi print. Pilih printer yang tidak aktif kerja
7. Tulis nama printer yang memproses plate di baris plate tersebut.
8. Ulangi langkah 1 di printer lainnya, apabila semua printer sedang mencetak/ditandai sticky notes, shift selesai

 
</details>

### 2.2 Rangkai
#### Kebutuhan
1. Komponen siap rangkai (dalam boks komponen)
2. Formulir `Checklist Komponen Rangkai` dicetak
3. Dokumen Asembly Sequence (terdapat di sub-folder Main Body Cut patung) dicetak
4. Lem Alteco 10 pcs
5. Lakban Kertas 1 pcs
6. 3D Printing Pen 1 pcs (opsional)
7. Kawat (opsional)
8. Gambar perspektif 3 sudut sebagai referensi dicetak
9. Akses ke Google Drive 3D Printing
10. Aplikasi STL Viewer [Babylonjs](https://www.babylonjs.com/)
11. Laptop/Komputer
12. Staff rangkai 2 orang
13. Cutter 2 pcs

#### Langkah
##### Persiapan
- Siapkan semua kebutuhan rangkai. Plot staff untuk merangkai
- Transfer item kebutuhan yang sudah dicetak ke lokasi rangkai yang disetujui
- Verifikasi hasil print komponen menggunakan Checklist Komponen Rangkai
  - **Absensi tiap komponen** dengan mengecek part number pada komponen dengan **blok spidol** nomor pada formulir
  - Kelompokan komponen dalam kelas per 10 nomor (1-10. 20-30) untuk mempermudah pencarian saat rangkai
  - Pisahkan komponen High Priority dengan Main Body Cut
  - Nomor di Checklist Komponen Rangkai yang tidak diblok spidol dicek dengan nama file di Subfolder Main Body Cut patung
    - Apabila file dengan nomor tersebut memiliki **label `tiny`**, **silang** nomor itu. Jika **tidak tiny**, **lingkari**.
    - Apabila filenya tidak ada, berarti nomor tersebut tidak diperlukan dalam proses rangkai
    - setelah diverifikasi, perintahkan staff 3d Printer untuk melakukan proses cetak komponen dengan nomor yang dilingkari. Transfer ke lokasi rangkai setelah dicetak.
##### Rangkai
- Mengikuti Dokumen Assembly Seqeuence, rangkai komponen secara urut dari awal sampai akhir.
  - Gunakan lem G untuk menempelkan sambungan antar komponen
  - >Komponen tiny (komponen dengan nomor yang disilang) tidak akan dicetak. Hiraukan saat rangkai.
##### Kirim
- Jadwalkan untuk pengiriman ke/penjemputan oleh supplier
---


## 3. Arsip & Manajemen Data

**Google Drive — Struktur Folder**
**Linke:** [GDrive](https://drive.google.com/drive/folders/1eSAQJrRWF6qD_M45ju9KKmKAiFJgmxj6)

Nama Folder: * **NamaProyek - Ukuran - ID Barang**

* **NamaProyek - Model 3D**

  * Upload model 3D sebelum pemotongan (`NamaProyek - Model 3D`)
* **NamaProyek - High Priority Cut**

  * Upload file hasil potong high priority (Blender) (`NamaProyek - HIGH PRIORITY`)
* **NamaProyek - Main Body Cut**

  * Upload folder hasil modular cutting (LuBAN) (`NamaProyek - MAIN BODY CUT`)
* **NamaProyek - Plate**

  * Upload file project Bambu Studio yang sudah di-slice (`NamaProyek - PLATE`)
* **File lain** seperti File 3D, File untuk Luban, bisa disimpan di dalam folder **NamaProyek - Ukuran - ID Barang**

> Semua file wajib diberi nama sesuai format proyek untuk keterlacakan.

## 4. Prosedur Tambahan
**Dokumentasi Garis Potong Mould Cor Mas Habib**
- Komunikasi dengan Mas Habib dan Mas Margono untuk hal berikut
  - Mas Habib/Mas Margono untuk mengelas titik seluruh komponen patung menjadi bentuk jadi, tapi belum dilas isi
  - Dokumentasi hasil potong seluruh patung dari banyak sudut
    - 4 sudut depan belakang samping kanan-kiri seluruh tubuh
    - bagian bawah dan yang tidak terlihat dari luar
    - maksimalkan luas foto untuk dokumentasi barang
- Kirim foto ke Bagian Produksi (Naufan/Egi) untuk pengumpulan hasil dokumentasi
- Upload ke dalam folder penyimpanan, sub folder Potongan Cor

## 5. Masalah dan Penyelesaian
Masalah dan Penyelesaian
* Tidak ada checklist
  - Kontak PIC 3D Printer untuk posisi checklist
  - Apabila checklist tidak ditemukan, buat catatan di kertas berisi nama komponen yang di print dan nama printer yang memproses, laporkan ke PIC 3D printer
* Printer tidak ada komponennya
  - Abaikan langkah 2-5
* Printer berhenti di tengah jalan (ciri-ciri: kontroler tidak menunjukan status “Print Finished”, Kepala printer berhenti di tengah dan tidak kembali ke area rumah/belakang)
  - Tempel sticky note “Mati Listrik”, tinggalkan printer
* Gagal cetak (ciri-ciri: hasil printer seperti kawat)
  - Tempel sticky note “Gagal Cetak”, tinggalkan printer
* Tidak ada kode komponen
  - Cek checklist untuk nama printer tempat komponen dicetak dan belum dicentang kolom “Selesai?”-nya. Cek nama platnya
  - Tulis nama plat di komponen, centang kolom “Selesai?”, dan lanjut ke langkah 6
* Tidak ada boks komponen
  - Kontak PIC 3D printer untuk posisi boks komponen
  - Cari boks tidak terpakai di dalam ruangan 3D Printer, beri label sesuai kode komponen
  - Apabila tidak ada solusi boks komponen, taruh di posisi yang mudah terlihat dan laporkan ke PIC 3D Printer
* Boks komponen tidak punya kode komponen
  - Tulis kode komponen dari item yang akan dimasukan ke dalam boks itu
* Komponen susah dilepas
  - Keluarkan plat dari mesin, lengkungkan plat untuk melepaskan komponen dari plat
* Nama plate yang dicari tidak ada di dalam printer
  - Hiraukan, cari nama plate lain
* Printer gagal menghasilkan lapisan cetakan pertama
  - Stop proses print
  - Tempel sticky note “GAGAL CETAK”, tinggalkan printer
* Komponen ringkih/remuk/tidak kokoh/
  * Catat part number komponen
  * cari file dengan part number itu di sub folder main body cut/high priority
  * cetak ulang komponen tersebut
- komponen yang rusak tidak ada part numbernya
  - catat nama plate yang dicetak oleh printer terkait
  - cek file Plate barang, cari nomor plat yang dicatat
  - cari komponen yang mirip dengan komponen rusak terkait. Tulis part number, antrikan cetak setelah semua komponen lain tercetak