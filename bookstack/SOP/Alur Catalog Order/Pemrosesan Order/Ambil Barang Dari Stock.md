---
bookstack_type: page
bookstack_id: 468
name: Ambil Barang Dari Stock
slug: ambil-barang-dari-stock
book_id: 36
chapter_id: 22
created_at: '2026-03-17T14:45:13.000000Z'
updated_at: '2026-04-08T07:16:54.000000Z'
source_url: null
---

**Tujuan:**  
Menggunakan barang dalam stock untuk mempercepat pemenuhan pesanan

**Trigger:**  
Sales order terbuat dan item tersedia di stock

**Input:**  
- Dokumen sales order
- Data stock warehouse

**Langkah:**  
1. Review sales order untuk barang stock
2. Konfirmasi barang stock ada di lokasinya
3. Buat [dokumen transfer material]()

**Output:**  
Barang stock tersedia di warehouse produksi