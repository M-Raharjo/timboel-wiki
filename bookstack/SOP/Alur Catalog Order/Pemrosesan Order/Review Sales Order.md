---
bookstack_type: page
bookstack_id: 480
name: Review Sales Order
slug: review-sales-order
book_id: 36
chapter_id: 22
created_at: '2026-03-18T05:08:07.000000Z'
updated_at: '2026-04-08T08:09:36.000000Z'
source_url: null
---

**Tujuan:**  
Menentukan apa saja yang harus dilakukan setelah sales order masuk

**Trigger:**
Sales order sudah dibuat

**Input:**
- Dokumen sales order
- Bukti Down Payment ada
- Data stock warehouse

**Desisi:**
- Stock ada -> [Ambil barang dari stock](https://wiki.pttimboel.com/link/468)
- Stock kosong -> [Buat order produksi](https://wiki.pttimboel.com/link/469)

**OutputL:**  
Metode pemenuhan pesanan ditentukan