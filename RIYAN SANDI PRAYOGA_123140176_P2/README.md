# 🌙 Personal Dashboard Sandi

## 📘 Deskripsi Singkat
**Personal Dashboard Sandi** adalah aplikasi web sederhana berbasis **JavaScript ES6+** yang berfungsi untuk membantu mengatur kegiatan harian seperti **jadwal kuliah**, **daftar tugas**, dan **catatan pribadi**.  
Semua data disimpan di **localStorage**, sehingga informasi tetap tersimpan walaupun halaman direfresh.

Aplikasi ini dirancang dengan **tampilan modern bergaya Glassmorphism**, responsif untuk semua ukuran layar (PC, tablet, dan smartphone), serta menggunakan animasi lembut untuk pengalaman pengguna yang elegan dan nyaman.

---

## 🧩 Fitur Utama
1. 🗓️ **Jadwal Kuliah**  
   - Tambah, hapus, dan simpan jadwal kuliah ke localStorage.
2. ✅ **Daftar Tugas**  
   - Tambah dan hapus daftar tugas dengan tampilan dinamis.
3. 📝 **Catatan Pribadi**  
   - Menyimpan catatan secara otomatis di localStorage.
4. ⏰ **Jam Real-time**  
   - Menampilkan waktu yang terus diperbarui setiap detik menggunakan async/await.
5. 🎨 **Desain Mewah dan Responsif**  
   - Menggunakan efek glassmorphism, animasi hover, dan tata letak grid modern.
6. 💾 **Penyimpanan Lokal (localStorage)**  
   - Semua data tetap tersimpan bahkan setelah browser ditutup.

---

## 🧠 Implementasi Fitur ES6+
Aplikasi ini mengimplementasikan berbagai fitur modern **JavaScript (ES6+)** seperti:

| Fitur ES6+ | Implementasi |
|-------------|--------------|
| **let & const** | Digunakan untuk semua deklarasi variabel agar scope lebih aman dan efisien |
| **Arrow Functions (≥3)** | `renderList`, `updateClock`, `getData`, `saveData` |
| **Template Literals** | Digunakan untuk membuat elemen HTML dinamis seperti daftar jadwal dan tugas |
| **Async / Await** | Diterapkan pada fungsi `updateClock` untuk memperbarui jam secara asinkron |
| **Classes** | Class `DashboardManager` digunakan untuk mengelola data dari setiap bagian dashboard (jadwal dan tugas) |

---


