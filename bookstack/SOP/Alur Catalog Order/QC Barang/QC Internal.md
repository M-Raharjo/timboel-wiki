---
bookstack_type: page
bookstack_id: 471
name: QC Internal
slug: qc-internal-UE8
book_id: 36
chapter_id: 23
created_at: '2026-03-17T14:46:27.000000Z'
updated_at: '2026-03-18T06:51:05.000000Z'
source_url: null
---

**Tujuan:**  
Memastikan hasil produksi barang sesuai dengan standar perusahaan

**Trigger:**  
Barang siap di area QC  

**Input:**  
- Sales order
- Checklist QC Internal
- Barang selesai produksi

**Langkah:**  
1. Konfirmasi jenis barang sesuai dengan sales order
2. Konfirmasi jumlah barang sesuai dengan sales order
3. Jalankan checklist QC internal

**Desisi:**
- Jika barang lulus QC -> Tandai QC complete
- Jika barang tidak lulus -> Tulis alasan, kembalikan ke produksi untuk perbaikanm

**Output:**  
Status barang lulus QC atau perlu perbaikan