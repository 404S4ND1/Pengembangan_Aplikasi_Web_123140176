📚 Sistem Manajemen Perpustakaan Sederhana
Sistem manajemen perpustakaan berbasis OOP (Object-Oriented Programming) yang diimplementasikan menggunakan Python. Sistem ini mendemonstrasikan konsep-konsep OOP seperti Abstract Class, Inheritance, Encapsulation, dan Polymorphism.

🎯 Fitur-Fitur
1. Manajemen Item Perpustakaan
Menambahkan Item: Menambahkan buku dan majalah ke koleksi perpustakaan
Menampilkan Daftar: Melihat semua item yang tersedia dengan status (tersedia/dipinjam)
Pencarian: Mencari item berdasarkan judul atau ID
Peminjaman: Meminjam item dari perpustakaan
Pengembalian: Mengembalikan item yang telah dipinjam
2. Tipe Item yang Didukung
Buku (Book): Dengan informasi ISBN, jumlah halaman, dan genre
Majalah (Magazine): Dengan informasi nomor edisi dan bulan publikasi
🏗️ Struktur Kode dan Konsep OOP
1. Abstract Class (LibraryItem)
python
class LibraryItem(ABC):
    # Base class untuk semua item perpustakaan
    # Menerapkan abstraction dengan abstract methods
Kelas dasar abstrak yang menjadi blueprint untuk semua item perpustakaan
Memiliki abstract methods: display_info() dan get_item_type()
Menerapkan encapsulation dengan private attributes (__item_id, __title)
2. Inheritance (Pewarisan)
python
class Book(LibraryItem):      # Mewarisi dari LibraryItem
class Magazine(LibraryItem):  # Mewarisi dari LibraryItem
Book dan Magazine mewarisi properties dan methods dari LibraryItem
Setiap subclass mengimplementasikan abstract methods sesuai karakteristiknya
3. Encapsulation
Private Attributes (__attribute): Tidak dapat diakses langsung dari luar class
__item_id, __title, __isbn, dll.
Protected Attributes (_attribute): Dapat diakses oleh subclass
_is_available
Property Decorators: Mengontrol akses ke private attributes
python
  @property
  def title(self):
      return self.__title
  
  @title.setter
  def title(self, value):
      # Validasi sebelum set value
4. Polymorphism
Method display_info() diimplementasikan berbeda di setiap subclass
Method yang sama menghasilkan output berbeda sesuai tipe object
python
# Polymorphism in action
for item in items:
    print(item.display_info())  # Output berbeda untuk Book dan Magazine
5. Composition
Class Library mengkomposisikan list dari LibraryItem
Mengelola koleksi objects dari berbagai tipe
📋 Persyaratan Sistem
Python 3.7 atau lebih tinggi
Tidak memerlukan library eksternal (menggunakan standard library)
🚀 Cara Menjalankan Program
1. Clone atau Download Repository
bash
git clone <repository-url>
cd library-management-system
2. Jalankan Program
bash
python library_system.py
3. Output yang Diharapkan
Program akan menampilkan demonstrasi lengkap dari semua fitur:

Menambahkan item (buku dan majalah)
Menampilkan semua item
Mencari item berdasarkan judul dan ID
Meminjam dan mengembalikan item
Menampilkan status perpustakaan
📸 Screenshot Hasil Running Program
1. Menambahkan Item ke Perpustakaan
📝 MENAMBAHKAN ITEM KE PERPUSTAKAAN:
------------------------------------------------------------
✓ Item 'Pemrograman Python untuk Pemula' berhasil ditambahkan!
✓ Item 'Data Science dengan Python' berhasil ditambahkan!
✓ Item 'Seni Menulis Kode Bersih' berhasil ditambahkan!
✓ Item 'Tech Monthly' berhasil ditambahkan!
✓ Item 'Science Today' berhasil ditambahkan!
2. Menampilkan Semua Item
============================================================
PERPUSTAKAAN PERPUSTAKAAN KOTA
============================================================
Total Item    : 5
Tersedia      : 5
Dipinjam      : 0
============================================================

============================================================
Tipe Item    : Buku
ID           : B001
Judul        : Pemrograman Python untuk Pemula
Penulis      : John Doe
Tahun        : 2023
ISBN         : 978-1234567890
Halaman      : 350
Genre        : Teknologi
Status       : ✓ Tersedia
============================================================
3. Mencari dan Meminjam Item
🔍 MENCARI ITEM BERDASARKAN JUDUL 'Python':
------------------------------------------------------------
[Menampilkan hasil pencarian...]

📤 MEMINJAM ITEM:
------------------------------------------------------------
✓ Item 'Pemrograman Python untuk Pemula' berhasil dipinjam!
✓ Item 'Tech Monthly' berhasil dipinjam!
📊 Diagram Class
                    ┌─────────────────┐
                    │  LibraryItem    │
                    │    (Abstract)   │
                    ├─────────────────┤
                    │ - __item_id     │
                    │ - __title       │
                    │ - __author      │
                    │ - __year        │
                    │ # _is_available │
                    ├─────────────────┤
                    │ + display_info()│
                    │ + get_item_type()│
                    │ + borrow()      │
                    │ + return_item() │
                    └────────┬────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
        ┌───────▼────────┐       ┌───────▼────────┐
        │     Book       │       │   Magazine     │
        ├────────────────┤       ├────────────────┤
        │ - __isbn       │       │ - __issue_num  │
        │ - __pages      │       │ - __month      │
        │ - __genre      │       └────────────────┘
        └────────────────┘
        
                    ┌─────────────────┐
                    │    Library      │
                    ├─────────────────┤
                    │ - __name        │
                    │ - __items[]     │
                    ├─────────────────┤
                    │ + add_item()    │
                    │ + search()      │
                    │ + display_all() │
                    │ + borrow_item() │
                    │ + return_item() │
                    └─────────────────┘
🔍 Penjelasan Konsep OOP yang Diterapkan
1. Abstract Class (30%)
LibraryItem adalah abstract base class dengan ABC
Mendefinisikan abstract methods yang wajib diimplementasikan
Menyediakan struktur dasar untuk semua item perpustakaan
2. Encapsulation (25%)
Private attributes (__attribute) untuk menyembunyikan data internal
Property decorators untuk kontrol akses yang lebih baik
Getter dan Setter dengan validasi data
Contoh: __item_id tidak bisa diakses langsung, hanya melalui property item_id
3. Polymorphism (20%)
Method display_info() memiliki implementasi berbeda di Book dan Magazine
Method get_item_type() mengembalikan tipe yang berbeda
Satu interface, banyak implementasi
4. Inheritance (15%)
Book dan Magazine mewarisi dari LibraryItem
Reusability kode melalui pewarisan
Subclass dapat mengakses properties dan methods parent class
5. Fungsionalitas Program (15%)
Semua fitur berjalan dengan baik
Error handling untuk kasus edge cases
User-friendly output dengan emoji dan formatting
🎓 Dokumentasi Kode (10%)
Setiap class memiliki docstring yang menjelaskan fungsinya
Setiap method memiliki penjelasan parameter dan return value
Komentar inline untuk kode yang kompleks
Type hints untuk parameter dan return values
👨‍💻 Cara Mengembangkan
Anda dapat mengembangkan sistem ini dengan menambahkan:

Item baru: DVD, E-Book, Audiobook (buat class baru yang inherit dari LibraryItem)
Fitur peminjam: Class Member untuk mengelola data peminjam
Database: Integrasi dengan SQLite atau database lain
GUI: Tambahkan interface grafis dengan Tkinter atau PyQt
Denda: Sistem denda untuk keterlambatan pengembalian
Reservasi: Fitur untuk mereservasi item yang sedang dipinjam
📝 Lisensi
Project ini dibuat untuk keperluan pembelajaran dan tugas praktikum.

👤 Author
RIYAN SANDI PRAYOGA
123140176

Tugas Praktikum OOP Python
Sistem Manajemen Perpustakaan
⭐ Jika project ini membantu, jangan lupa beri star pada repository!

