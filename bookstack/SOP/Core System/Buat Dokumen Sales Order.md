---
bookstack_type: page
bookstack_id: 500
name: Buat Dokumen Sales Order
slug: buat-dokumen-sales-order
book_id: 37
chapter_id: null
created_at: '2026-03-29T14:46:59.000000Z'
updated_at: '2026-03-29T14:55:48.000000Z'
source_url: null
---

**Definisi:**
Sales order hanya digunakan untuk mencatat penjualan yang harus dipenuhi oleh produksi


**Input:**  
- Quotation client
- Purchase order client
- email
- whatsapp

**Langkah:**  
1. Buka kirun database
2. ctrl + G -> new sales order
3. Isi data customer
4. Isi delivery date (tanggal produksi selesai)
5. Isi customer purchase order (kalo ada)
6. [Upload file](https://docs.frappe.io/framework/user/en/desk/attachments) customer purchase order
7. Jika sudah ada quotation -> Get items from > quotation
8. Isi item sesuai dengan permintaan client
9. Diskon jika ada
10. Tentukan charges

**Output:**  
Data sales order untuk produksi