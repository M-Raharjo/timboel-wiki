---
bookstack_type: page
bookstack_id: 479
name: Terima Pembayaran DP
slug: terima-pembayaran-dp
book_id: 36
chapter_id: 21
created_at: '2026-03-18T04:43:56.000000Z'
updated_at: '2026-04-08T07:24:47.000000Z'
source_url: null
---

**Tujuan:**  
Meneripa down payment agar sales order dapat mulai di proses

**Aturan:**
- Delivery date sales order 8 minggu dari DP masuk ke bank

**Trigger:**  
- e-mail dari customer
- notifikasi pembayaran dari bank

**Input:**  
- Bukti transfer customer
- Sales order

**Langkah:**  
1. Review bukti transfer
2. Konfirmasi bukti transfer dengan uang masuk bank
3. [Input pembayaran]()

**Desisi:**
- jika pembayaran belum ditemukan -> info ke customer dan tunggu 2 hari kerja
- jika pembayaran ditemukan dan sesuai -> update delivery date

**Output:**  
Pembayaran DP terverifikasi, Delivery date pada sales order sudah di perbaharui