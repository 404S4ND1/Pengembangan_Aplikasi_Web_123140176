# Sistem Manajemen Perpustakaan Sederhana

Dokumentasi dan kode contoh untuk **Sistem Manajemen Perpustakaan** berbasis OOP (Python).

---

## Ringkasan

Sistem ini mendemonstrasikan konsep-konsep OOP:

* **Abstraction**: `LibraryItem` sebagai abstract base class.
* **Inheritance**: `Book` dan `Magazine` mewarisi `LibraryItem`.
* **Encapsulation**: atribut private (`__...`) dan property getter/setter.
* **Polymorphism**: method `display_info()` berbeda implementasinya.
* **Composition**: `Library` mengandung daftar `LibraryItem`.

Dibangun untuk Python 3.7+ dan tidak memerlukan library eksternal.

---

## Struktur Project

```
library-management-system/
├─ library_system.py    # file utama berisi semua class dan demo
└─ README.md            # dokumentasi (file ini)
```

---

## Kode: `library_system.py`

Salin seluruh blok ini ke file `library_system.py` dan jalankan `python library_system.py`.

```python
from abc import ABC, abstractmethod
from typing import List, Optional

class LibraryItem(ABC):
    """Blueprint abstrak untuk item perpustakaan.

    Menyimpan atribut privat untuk menerapkan encapsulation dan
    mendefinisikan interface yang harus diimplementasikan subclass.
    """

    def __init__(self, item_id: str, title: str, author: str, year: int):
        self.__item_id = item_id
        self.__title = title
        self.__author = author
        self.__year = year
        self._is_available = True  # protected attribute

    # Properties untuk encapsulation
    @property
    def item_id(self) -> str:
        return self.__item_id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        if not value:
            raise ValueError("Title tidak boleh kosong")
        self.__title = value

    @property
    def author(self) -> str:
        return self.__author

    @property
    def year(self) -> int:
        return self.__year

    @property
    def is_available(self) -> bool:
        return self._is_available

    def borrow(self) -> bool:
        """Coba pinjam item. Mengembalikan True jika berhasil."""
        if self._is_available:
            self._is_available = False
            return True
        return False

    def return_item(self) -> None:
        """Kembalikan item ke status tersedia."""
        self._is_available = True

    @abstractmethod
    def display_info(self) -> str:
        """Tampilkan informasi lengkap item (harus diimplementasikan subclass)."""

    @abstractmethod
    def get_item_type(self) -> str:
        """Kembalikan tipe item: 'Book' atau 'Magazine' dll."""


class Book(LibraryItem):
    """Representasi buku dengan fields tambahan seperti ISBN, pages, genre."""

    def __init__(self, item_id: str, title: str, author: str, year: int,
                 isbn: str, pages: int, genre: str):
        super().__init__(item_id, title, author, year)
        self.__isbn = isbn
        self.__pages = pages
        self.__genre = genre

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def pages(self) -> int:
        return self.__pages

    @property
    def genre(self) -> str:
        return self.__genre

    def display_info(self) -> str:
        status = "✓ Tersedia" if self.is_available else "✗ Dipinjam"
        return (f"Tipe Item : Buku\n"
                f"ID        : {self.item_id}\n"
                f"Judul     : {self.title}\n"
                f"Penulis   : {self.author}\n"
                f"Tahun     : {self.year}\n"
                f"ISBN      : {self.isbn}\n"
                f"Halaman   : {self.pages}\n"
                f"Genre     : {self.genre}\n"
                f"Status    : {status}\n")

    def get_item_type(self) -> str:
        return "Book"


class Magazine(LibraryItem):
    """Representasi majalah dengan issue number dan month."""

    def __init__(self, item_id: str, title: str, author: str, year: int,
                 issue_num: int, month: str):
        super().__init__(item_id, title, author, year)
        self.__issue_num = issue_num
        self.__month = month

    @property
    def issue_num(self) -> int:
        return self.__issue_num

    @property
    def month(self) -> str:
        return self.__month

    def display_info(self) -> str:
        status = "✓ Tersedia" if self.is_available else "✗ Dipinjam"
        return (f"Tipe Item : Majalah\n"
                f"ID        : {self.item_id}\n"
                f"Judul     : {self.title}\n"
                f"Penulis   : {self.author}\n"
                f"Tahun     : {self.year}\n"
                f"Edisi     : {self.issue_num}\n"
                f"Bulan     : {self.month}\n"
                f"Status    : {status}\n")

    def get_item_type(self) -> str:
        return "Magazine"


class Library:
    """Kelas untuk mengelola koleksi LibraryItem."""

    def __init__(self, name: str):
        self.__name = name
        self.__items: List[LibraryItem] = []

    def add_item(self, item: LibraryItem) -> None:
        self.__items.append(item)
        print(f"✓ Item '{item.title}' berhasil ditambahkan!")

    def display_all(self) -> None:
        total = len(self.__items)
        available = sum(1 for i in self.__items if i.is_available)
        borrowed = total - available
        print("=" * 60)
        print(self.__name.upper().center(60))
        print("=" * 60)
        print(f"Total Item    : {total}")
        print(f"Tersedia      : {available}")
        print(f"Dipinjam      : {borrowed}")
        print("=" * 60)
        for item in self.__items:
            print(item.display_info())
            print("=" * 60)

    def search_by_title(self, keyword: str) -> List[LibraryItem]:
        keyword_lower = keyword.lower()
        results = [i for i in self.__items if keyword_lower in i.title.lower()]
        return results

    def search_by_id(self, item_id: str) -> Optional[LibraryItem]:
        for i in self.__items:
            if i.item_id == item_id:
                return i
        return None

    def borrow_item(self, item_id: str) -> bool:
        item = self.search_by_id(item_id)
        if item is None:
            print(f"✗ Item dengan ID {item_id} tidak ditemukan.")
            return False
        if item.borrow():
            print(f"✓ Item '{item.title}' berhasil dipinjam!")
            return True
        else:
            print(f"✗ Item '{item.title}' sudah dipinjam.")
            return False

    def return_item(self, item_id: str) -> bool:
        item = self.search_by_id(item_id)
        if item is None:
            print(f"✗ Item dengan ID {item_id} tidak ditemukan.")
            return False
        item.return_item()
        print(f"✓ Item '{item.title}' berhasil dikembalikan!")
        return True


# Demo penggunaan
if __name__ == "__main__":
    lib = Library("Perpustakaan Kota")

    # Menambahkan beberapa item
    lib.add_item(Book("B001", "Pemrograman Python untuk Pemula", "John Doe", 2023,
                      "978-1234567890", 350, "Teknologi"))
    lib.add_item(Book("B002", "Data Science dengan Python", "Jane Smith", 2022,
                      "978-9876543210", 420, "Data"))
    lib.add_item(Book("B003", "Seni Menulis Kode Bersih", "Robert C.", 2021,
                      "978-1112223334", 280, "Pemrograman"))
    lib.add_item(Magazine("M001", "Tech Monthly", "Editor Team", 2024, 45, "November"))
    lib.add_item(Magazine("M002", "Science Today", "Science Org", 2024, 12, "Desember"))

    # Menampilkan semua item
    print()
    lib.display_all()

    # Mencari berdasarkan judul (keyword)
    print("\n🔍 MENCARI ITEM BERDASARKAN JUDUL 'Python':")
    results = lib.search_by_title("Python")
    if results:
        for r in results:
            print(r.display_info())
    else:
        print("Tidak ada hasil pencarian.")

    # Meminjam item
    print("\n📤 MEMINJAM ITEM:")
    lib.borrow_item("B001")
    lib.borrow_item("M001")

    # Status setelah peminjaman
    print()
    lib.display_all()

    # Mengembalikan item
    print("\n📥 MENGEMBALIKAN ITEM:")
    lib.return_item("B001")
    lib.return_item("M001")

    # Status akhir
    print()
    lib.display_all()
```

---

## Penjelasan Singkat

* `LibraryItem` mendefinisikan interface: `display_info()` dan `get_item_type()` harus diimplementasikan.
* `Book` dan `Magazine` menambahkan atribut khusus masing-masing.
* `Library` menyediakan operasi: `add_item`, `display_all`, `search_by_title`, `search_by_id`, `borrow_item`, `return_item`.

---

## Pengembangan Lebih Lanjut (Ide)

* Tambah class `Member` untuk melacak peminjam.
* Simpan data ke SQLite untuk persistensi.
* Tambah fitur denda dan durasi pinjam.
* GUI menggunakan Tkinter atau PyQt.

---

## Lisensi

Project ini dibuat untuk keperluan pembelajaran dan tugas praktikum.

---

## Author

**RIYAN SANDI PRAYOGA** — 123140176

*Tugas Praktikum OOP Python — Sistem Manajemen Perpustakaan*
