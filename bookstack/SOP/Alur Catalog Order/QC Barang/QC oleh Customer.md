---
bookstack_type: page
bookstack_id: 472
name: QC oleh Customer
slug: qc-oleh-customer
book_id: 36
chapter_id: 23
created_at: '2026-03-17T14:46:45.000000Z'
updated_at: '2026-03-18T06:59:53.000000Z'
source_url: null
---

**Tujuan:**  
Memberikan kesempatan kepada customer untuk melakukan verfikasi kualitas barang secara independen sebelum pengiriman

**Aturan:**
- QC hanya dilakukan pada barang yang sudah lulus QC internal
- QC hanya memeriksa barang sesuai sales order
- Perubahan design atau spefisikasi tidak diperbolehkan pada tahap ini

**Trigger:**  
Barang sudah lulus QC internal

**Input:**  
- Barang lulus QC
- Sales Order
- Kontak Customer

**Langkah:**  
1. Menjadwalkan waktu QC dengan customer
2. Siapkan barang di area QC agar mudah di periksa
3. Jelaskan pada customer spesifikasi barang sesuai sales order
4. Dampingi customer selama proses pemeriksaan
5. Catat hasil pemeriksaan customer

**Desisi:**
- Lulus QC customer -> Packing
- Tidak Lulus QC customer -> tulis alasan, kembalikan ke produksi untuk perbaikan

**Output:**  
Status QC barang oleh customer diketahui