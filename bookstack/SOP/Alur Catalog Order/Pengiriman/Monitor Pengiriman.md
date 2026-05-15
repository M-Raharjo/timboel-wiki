---
bookstack_type: page
bookstack_id: 481
name: Monitor Pengiriman
slug: monitor-pengiriman
book_id: 36
chapter_id: 25
created_at: '2026-03-18T07:36:20.000000Z'
updated_at: '2026-03-18T12:12:57.000000Z'
source_url: null
---

**Tujuan:**  
Memantau status pengiriman sampai barang diterima oleh customer dan memastikan dokumen pengiriman telah dikirim kepada pihak yang diperlukan.

**Trigger:**  
Barang telah diserahkan kepada jasa pengiriman (lokal) atau EMKL / forwarder (export)  

**Input:**  
- Sales Order
- Kontak customer
- Kontak jasa pengiriman / EMKL
- Nomor resi pengiriman (local)
- Informasi shipment dari EMKL (Export)
- Dokumen pengiriman

**Langkah:**  
1. Monitor status pengiriman melalui kontak jasa pengiriman / EMKL
2. Informasikan status pengiriman kepada customer bila diperlukan  
**(Langkah tambahan untuk export)**
3. Terima copy BL dari EMKL
4. Kirim copy BL ke customer untuk proses pembayaran

**Desisi:**
- Jika local -> Monitor status pengiriman dengan nomor resi sampai barang diterima customer
- Jika export -> Monitor status pengiriman sampai Copy BL diterbikan

**Output:**  
- Status pengiriman diketahui
- Customer mengetahui status pengiriman
- Copy BL sudah diterima customer