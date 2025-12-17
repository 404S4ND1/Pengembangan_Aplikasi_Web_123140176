# Tugas P6: Pengembangan Aplikasi Web (Pyramid Framework)

**Nama:** Riyan Sandi Prayoga  
**NIM:** 123140176  
**Mata Kuliah:** Pengembangan Aplikasi Web  

---

## 📝 Deskripsi Singkat
Repository ini berisi source code untuk **Tugas Pertemuan 6 (P6)**.
Pada tugas ini, saya mengimplementasikan kerangka kerja (framework) **Python Pyramid** untuk membangun aplikasi web, termasuk struktur routing, templating, dan manajemen view sederhana.

## 📂 Struktur Folder
* **pyramid/**: Berisi konfigurasi inti framework dan file inisialisasi.
* **mahasiswa/**: Modul aplikasi utama (views, models, dan templates).

---

## ⚙️ Cara Menjalankan (Installation & Run)

Berikut adalah langkah-langkah untuk menjalankan proyek ini di lingkungan lokal (Localhost):

### 1. Prasyarat
Pastikan Python 3 sudah terinstal di komputer.
```bash
python3 --version
2. Setup Virtual Environment
Disarankan menggunakan virtual environment agar dependensi tidak bentrok.

Bash

# Masuk ke direktori project
cd RIYAN_SANDI_PRAYOGA_123140176_P6

# Buat virtual environment
python3 -m venv venv

# Aktifkan virtual environment (Linux/Mac)
source venv/bin/activate
3. Instalasi Dependensi
Install paket pyramid dan dependensi lain yang dibutuhkan.

Bash

pip install pyramid
pip install -e .
4. Menjalankan Server
Jalankan development server menggunakan pserve.

Bash

pserve development.ini
Akses aplikasi di browser melalui:

👉 http://localhost:6543 (atau port yang tertera di terminal).

🛠️ Teknologi yang Digunakan
Language: Python 3

Framework: Pyramid Web Framework

Template Engine: Jinja2 / Chameleon (sesuai konfigurasi)

WSGI Server: Waitress (Default Pyramid)

📸 Screenshots
(Tampilan hasil run aplikasi)

[Tambahkan screenshot jika diperlukan]

Copyright © 2025 Riyan Sandi Prayoga.


### Cara Simpannya:
1.  Buka terminal, masuk ke folder P6 kamu:
    ```bash
    cd ~/Documents/PRKPAW/RIYAN_SANDI_PRAYOGA_123140176_P6
    ```
2.  Buat file README:
    ```bash
    nano README.md
    ```
3.  **Paste** kode di atas ke dalamnya.
4.  Simpan (`Ctrl+O` > Enter) dan Keluar (`Ctrl+X`).
5.  Jangan lupa **add, commit, dan push** lagi ke GitHub supaya README-nya muncul:
    ```bash
    git add README.md
    git commit -m "Add README documentation for P6"
    git push -u origin main
    ```
