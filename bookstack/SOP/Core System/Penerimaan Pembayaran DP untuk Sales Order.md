---
bookstack_type: page
bookstack_id: 518
name: Penerimaan Pembayaran DP untuk Sales Order
slug: penerimaan-pembayaran-dp-untuk-sales-order
book_id: 37
chapter_id: null
created_at: '2026-04-08T07:24:08.000000Z'
updated_at: '2026-04-08T07:39:56.000000Z'
source_url: null
---

**Tujuan:**  
Menerima Pembayaran DP untuk Sales Order


**Trigger:**  
Notifikasi adanya pembarayan dari sales atau customer

**Input:**  
- Bukti pembayaran
- Nomor sales order

**Langkah:**  
1. Buka [kirun database](https://kirun.pttimboel.com)
2. Ctrl + g -> Payment entry list
3. New payment entry
4. Payment type -> Recieve
5. Isi party type -> Customer
6. Isi party sesuai customer sales order
7. Isi jumlah yang di terima
8. Isi payment references untuk referensi pembayaran ini untuk apa saja, dan alokasinya per referensi
9. Isi refernsi bukti pembayaran
10. Isi tanggal bukti pembayaran
12. Save
13. Upload bukti pembayaran sebagai attachment
14. Submit

**Output:**  
Pemayaran diterima di sistem, lengkap dengan referensi untuk apa dan referensi pembayaran