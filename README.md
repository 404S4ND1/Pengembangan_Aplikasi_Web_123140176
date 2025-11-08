# 📖 Personal Book Manager

Aplikasi **Manajemen Buku Pribadi** yang memungkinkan pengguna mencatat, mengelola, dan mencari buku yang dimiliki, sedang dibaca, atau ingin dibeli. Dibangun menggunakan **React** dengan penerapan **Context API**, **React Router**, dan **Hooks**.

---

## 🚀 Fitur Utama

* **Tambah Buku Baru** (judul, penulis, status: *dimiliki / sedang dibaca / ingin dibeli*)
* **Edit dan Hapus Buku**
* **Filter Buku** berdasarkan status
* **Cari Buku** (lokal & via API [OpenLibrary](https://openlibrary.org/developers/api))
* **Penyimpanan permanen** dengan `localStorage`
* **Statistik Buku** (jumlah buku per status)

---

## 🧱 Teknologi yang Digunakan

* **React 18+** (Functional Components & Hooks)
* **React Router DOM v6**
* **Context API** (state management global)
* **Custom Hooks**: `useLocalStorage` & `useBookStats`
* **OpenLibrary API** untuk pencarian buku online
* **React Testing Library** untuk unit test

---

## 📂 Struktur Folder

```bash
src/
├── components/
│   ├── BookForm/
│   │   └── BookForm.js
│   ├── BookList/
│   │   └── BookList.js
│   └── BookFilter/
│       └── BookFilter.js
│
├── context/
│   └── BookContext.js
│
├── hooks/
│   ├── useLocalStorage.js
│   └── useBookStats.js
│
├── pages/
│   ├── Home/
│   │   └── Home.js
│   └── Stats/
│       └── Stats.js
│
├── tests/
│   ├── BookForm.test.js
│   ├── BookList.test.js
│   ├── BookFilter.test.js
│   ├── useLocalStorage.test.js
│   └── useBookStats.test.js
│
├── App.js
├── styles.css
└── index.js
```

---

## ⚙️ Cara Instalasi dan Menjalankan

### 1️⃣ Clone repository ini

```bash
git clone https://github.com/username/personal-book-manager.git
cd personal-book-manager
```

### 2️⃣ Install dependencies

```bash
npm install
```

### 3️⃣ Jalankan aplikasi

```bash
npm start
```

### 4️⃣ Buka di browser

```
http://localhost:3000
```

---

## 🧩 Custom Hooks

### `useLocalStorage`

Hook ini digunakan untuk menyimpan dan mengambil data buku dari localStorage agar data tetap ada meskipun halaman direfresh.

### `useBookStats`

Hook ini menghitung statistik jumlah buku berdasarkan status: dimiliki, sedang dibaca, atau ingin dibeli.

---

## 🧠 Fitur React yang Digunakan

| Fitur          | Deskripsi                                                                 |
| -------------- | ------------------------------------------------------------------------- |
| `useState`     | Menyimpan dan memperbarui state lokal seperti daftar buku atau input form |
| `useEffect`    | Sinkronisasi data dengan localStorage dan API OpenLibrary                 |
| `useContext`   | Mengelola state global antar komponen dengan Context API                  |
| `React Router` | Navigasi antar halaman (Home dan Stats)                                   |
| `Custom Hooks` | Reusable logic untuk penyimpanan dan statistik buku                       |

---

## 🧪 Testing

Terdapat **5 unit test** menggunakan **React Testing Library**, meliputi:

* Form input dan validasi
* Penambahan & penghapusan buku
* Filter berdasarkan status
* Hook `useLocalStorage`
* Hook `useBookStats`

Jalankan perintah berikut untuk testing:

```bash
npm test
```

Tambahkan screenshot hasil test di folder `/tests/screenshots/` untuk laporan dokumentasi.

---

## ⚠️ Error Handling

* Validasi input: judul & penulis wajib diisi.
* Jika API OpenLibrary gagal diakses, aplikasi menampilkan pesan error dan tetap berfungsi dengan data lokal.

---

## 🖼️ Screenshot Antarmuka

### Halaman Home

Menampilkan daftar buku, filter, pencarian, dan tombol tambah buku.

### Halaman Statistik

Grafik jumlah buku berdasarkan status (dimiliki, sedang dibaca, ingin dibeli).

*(Tambahkan screenshot nyata dari aplikasi kamu di sini setelah dijalankan)*

---

## ✍️ Catatan Developer

* Dibuat dengan ❤️ oleh mahasiswa untuk proyek React.
* Didesain agar tampak natural dan terstruktur seperti aplikasi produksi.
* Memiliki modularitas tinggi dan mudah dikembangkan.

---

## 📜 Lisensi

MIT License - silakan gunakan dan modifikasi sesuai kebutuhan.
