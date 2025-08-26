---
title: "03. proyek"
weight: 3
bookCollapseSection: true
---
# proyek

Setiap proyek punya file sendiri. Minimal buat **Ringkasan** dan **Checklist**. Tambahkan `Jadwal`, `Catatan rapat`, `Lampiran` bila perlu.

Copy-Paste Template berikut saat membuat proyek baru

```
---
nama: sample_project
type: custom_order # custom_order | perintah_kerja | pengembangan
status: progress # baru | progress
dibuat: YYYY-MM-DD
deadline: YYYY-MM-DD
---

# Template proyek

## Ringkasan Adiksimba
- apa: 
- dimana: 
- kapan: 
- siapa: 
- mengapa: 
- bagaimana: 

[catatan]: # (untuk perintah kerja hanya butuh: apa, siapa, kapan)

## Checklist
- [ ] Langkah langkah utama yang harus diselesaikan

[contoh]: # (confirm design, model kecil, dp, produksi model)

## Jadwal (opsional)
- [ ] Jadwal aktivitas penting + tanggal deadline
- [ ] Format: nama kegiatan, YYYY-MM-DD

## Hasil Rapat (opsional)
### Rapat YYYY-MM-DD
- Point keputusan rapat ditulis disini
- Gunakan bullet list supaya mudah dibaca


## Lampiran (opsional)
- Daftar dokumen yang dibutuh kan proyek

[contoh]: # (foto, 3d model, gambar lapangan, pdf)
```