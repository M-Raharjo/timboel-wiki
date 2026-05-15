---
bookstack_type: page
bookstack_id: 465
name: Negosiasi Dengan Customer
slug: negosiasi-dengan-customer
book_id: 36
chapter_id: 20
created_at: '2026-03-17T14:44:14.000000Z'
updated_at: '2026-03-27T03:02:45.000000Z'
source_url: null
---

**Tujuan:**  
Mendapatkan persetujuan dengan customer mengenai harga dan terms

**Aturan:**
- Diskon gunakan diskon rule

**Trigger:**  
- Customer meminta diskon atau keringanan lain

**Input:**  
- Quotation yang sudah dikirim
- History dengan customer (jika ada, contoh: relasi personal, transaksi sebelumnya)
- Perjanjian tertulis dengan customer
- Nilai order
- Diskon rule

**Langkah:**  
1. Tanya bagian mana dari quotation yang keberatan (harga, jumlah, shipping atau terms)
2. Evaluasi permintaan customer, [sesuaikan fitur](https://wiki.pttimboel.com/link/495)
3. Jika belum setuju, berikan diskon sesuai dengan [diskon rule](https://wiki.pttimboel.com/link/44)
4. Jika masih belum setuju, eskalasi ke atasan
5. Konfirmasi kembali dengan customer tentang hal yang sudah di setujui
6. Update Quotation sesuai dengan persetujuan

**Output:**  
Dokumen quotation dengan data hasil diskusi