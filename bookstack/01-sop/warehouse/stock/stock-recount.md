---
name: Stock Recount
tags:
  Department: Warehouse
  System: ERPNext
---

# Stock Recount

## Tujuan

Menyamakan stok fisik dengan catatan ERPNext.

## Trigger

Jadwal stock opname atau ditemukan selisih stok.

## Input

- Daftar item
- Lokasi warehouse
- Catatan stok ERPNext

## Langkah

1. Bekukan pergerakan stok untuk area yang dihitung.
2. Hitung stok fisik.
3. Catat selisih.
4. Verifikasi ulang item dengan selisih besar.
5. Buat Stock Reconciliation jika angka sudah disetujui.

## Output

Stok ERPNext sesuai hasil hitung fisik.
