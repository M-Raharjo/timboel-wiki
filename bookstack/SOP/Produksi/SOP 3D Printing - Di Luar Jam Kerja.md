---
bookstack_type: page
bookstack_id: 424
name: SOP 3D Printing - Di Luar Jam Kerja
slug: sop-3d-printing-di-luar-jam-kerja
book_id: 33
chapter_id: null
created_at: '2026-02-13T07:27:44.000000Z'
updated_at: '2026-02-13T07:30:19.000000Z'
source_url: null
---

# SOP SHIFT MALAM – 3D PRINT

## 🎯 Tujuan
Menjaga uptime printer dengan melanjutkan proses cetak sesuai daftar plate pada Checklist.

Checklist adalah sumber kebenaran utama status pekerjaan.
Tidak boleh mencetak sebelum melakukan cross-check dengan checklist.

---

## ⚠️ Batasan Staff Malam

Staff malam:

- Tidak melakukan troubleshooting
- Tidak mengubah setting printer
- Tidak mengganti filament
- Tidak mengubah file
- Tidak mencetak sebelum cross-check checklist

---

## 🕒 Waktu Pemeriksaan

Dilakukan pada jam yang telah ditentukan (pukul 20-23, pukul 04-06).

---

# 🔁 Prosedur Pemeriksaan

## 1️⃣ Cek Printer yang Berhenti

Kelilingi semua printer:

- Jika masih mencetak → Tidak perlu tindakan.
- Jika sudah selesai → Lanjut ke langkah 2.
- Jika error → Jangan disentuh. Biarkan untuk shift pagi.

---

## 2️⃣ Tandai Plate Selesai

Di Checklist:

Cari baris di mana:
- Kolom Printer berisi nama printer tersebut.
- Kolom Selesai? belum dicentang.

Kemudian:
- Beri tanda centang (✓) pada kolom Selesai?.

Jangan menghapus nama printer.

---

## 3️⃣ Bersihkan dan Reset Printer

- Lepas hasil cetakan dengan hati-hati.
- Bersihkan build plate bila perlu.
- Pasang kembali build plate dengan benar dan rata.

---

## 4️⃣ Cross-Check Sebelum Print

Di printer:

1. Buka File List.
2. Lihat daftar plate yang tersedia di printer.

Kemudian di Checklist:

- Cari plate yang tersedia di printer.
- Pastikan plate tersebut belum dicentang pada kolom Selesai?.

Jika plate tersedia dan belum dicentang:

1. Tulis nama printer pada kolom Printer di baris plate tersebut.
2. Setelah itu tekan Print pada printer.

Dilarang mencetak sebelum memastikan plate belum dicentang di Checklist.

---

## 5️⃣ Selesai

Tinggalkan ruangan dan kembali pada jadwal pemeriksaan berikutnya.

---

# 📌 Logika Status Checklist

- Printer kosong & Selesai kosong → Belum dicetak
- Printer terisi & Selesai kosong → Sedang dicetak
- Printer terisi & Selesai dicentang → Sudah selesai

Checklist adalah pengendali utama alur kerja.