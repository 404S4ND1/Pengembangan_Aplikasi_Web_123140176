Program Pengelolaan Data Nilai Mahasiswa

Program ini dibuat untuk mengelola data nilai mahasiswa dengan berbagai fitur lengkap seperti perhitungan nilai akhir, penentuan grade, pencarian nilai tertinggi/terendah, filter berdasarkan grade, dan lain-lain.

Fitur Utama:
- Menampilkan data mahasiswa dalam format tabel
- Menambah data mahasiswa baru
- Menghitung nilai akhir berdasarkan bobot: 30% UTS + 40% UAS + 30% Tugas
- Menentukan grade berdasarkan nilai akhir:
    • A: ≥80  
    • B: ≥70  
    • C: ≥60  
    • D: ≥50  
    • E: <50
- Mencari mahasiswa dengan nilai tertinggi dan terendah
- Memfilter mahasiswa berdasarkan grade (A/B/C/D/E)
- Menghitung rata-rata nilai kelas

Struktur Data:
Data mahasiswa disimpan dalam bentuk list of dictionaries. Setiap mahasiswa memiliki atribut:
- nama (string)
- NIM (string)
- nilai_uts (angka 0–100)
- nilai_uas (angka 0–100)
- nilai_tugas (angka 0–100)

Contoh data:
{
  "nama": "Ahmad Rizki",
  "nim": "230101",
  "nilai_uts": 85,
  "nilai_uas": 90,
  "nilai_tugas": 88
}

Cara Menjalankan:
1. Pastikan Python 3 terinstal di komputer.
2. Simpan kode program dalam file Python (misal: nilai_mahasiswa.py).
3. Buka terminal atau command prompt.
4. Jalankan dengan perintah:
   python nilai_mahasiswa.py

Catatan: Program ini tidak memerlukan library tambahan. Semua tampilan tabel dibuat menggunakan print biasa.

Tampilan Program:
Program menggunakan menu interaktif berbasis teks:
1. Tampilkan Semua Data
2. Tambah Data Mahasiswa Baru
3. Cari Mahasiswa dengan Nilai Tertinggi
4. Cari Mahasiswa dengan Nilai Terendah
5. Filter Mahasiswa Berdasarkan Grade
6. Hitung Rata-rata Nilai Kelas
7. Keluar

Pengguna cukup memasukkan angka sesuai pilihan.

Validasi dan Keamanan:
- Input nilai divalidasi (harus angka antara 0 sampai 100).
- Program menangani kesalahan input (misalnya memasukkan huruf di nilai) tanpa crash.

Informasi Mahasiswa:
Nama    : Riyansandi Prayoga  
NIM     : 123140176  
Mata Kuliah: Pemrograman Komputer  
Tanggal : November 2025

Program ini dibuat sesuai dengan persyaratan tugas dan siap dijalankan tanpa konfigurasi tambahan.