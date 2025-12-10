from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional


class LibraryItem(ABC):
    """
    Abstract Base Class untuk semua item perpustakaan.
    Menerapkan konsep Abstraction dan Encapsulation.
    """
    
    def __init__(self, item_id: str, title: str, author: str, year: int):
        """
        Constructor untuk LibraryItem
        
        Args:
            item_id: ID unik item
            title: Judul item
            author: Penulis/pembuat item
            year: Tahun publikasi
        """
        self.__item_id = item_id  # Private attribute (Encapsulation)
        self.__title = title
        self.__author = author
        self.__year = year
        self._is_available = True  # Protected attribute
    
    # Property decorator untuk encapsulation
    @property
    def item_id(self) -> str:
        """Getter untuk item_id"""
        return self.__item_id
    
    @property
    def title(self) -> str:
        """Getter untuk title"""
        return self.__title
    
    @title.setter
    def title(self, value: str):
        """Setter untuk title dengan validasi"""
        if value and len(value) > 0:
            self.__title = value
        else:
            raise ValueError("Title tidak boleh kosong")
    
    @property
    def author(self) -> str:
        """Getter untuk author"""
        return self.__author
    
    @property
    def year(self) -> int:
        """Getter untuk year"""
        return self.__year
    
    @property
    def is_available(self) -> bool:
        """Getter untuk status ketersediaan"""
        return self._is_available
    
    @abstractmethod
    def display_info(self) -> str:
        """
        Abstract method yang harus diimplementasikan oleh subclass.
        Menampilkan informasi lengkap item.
        """
        pass
    
    @abstractmethod
    def get_item_type(self) -> str:
        """
        Abstract method untuk mendapatkan tipe item.
        """
        pass
    
    def borrow(self) -> bool:
        """
        Method untuk meminjam item.
        Returns:
            True jika berhasil, False jika item tidak tersedia
        """
        if self._is_available:
            self._is_available = False
            return True
        return False
    
    def return_item(self) -> bool:
        """
        Method untuk mengembalikan item.
        Returns:
            True jika berhasil
        """
        self._is_available = True
        return True
    
    def __str__(self) -> str:
        """String representation untuk object"""
        status = "Tersedia" if self._is_available else "Dipinjam"
        return f"[{self.item_id}] {self.title} - {status}"


class Book(LibraryItem):
    """
    Class Book yang mewarisi dari LibraryItem.
    Menerapkan konsep Inheritance dan Polymorphism.
    """
    
    def __init__(self, item_id: str, title: str, author: str, year: int, 
                 isbn: str, pages: int, genre: str):
        """
        Constructor untuk Book
        
        Args:
            item_id: ID unik buku
            title: Judul buku
            author: Penulis buku
            year: Tahun publikasi
            isbn: ISBN buku
            pages: Jumlah halaman
            genre: Genre buku
        """
        super().__init__(item_id, title, author, year)
        self.__isbn = isbn
        self.__pages = pages
        self.__genre = genre
    
    @property
    def isbn(self) -> str:
        """Getter untuk ISBN"""
        return self.__isbn
    
    @property
    def pages(self) -> int:
        """Getter untuk pages"""
        return self.__pages
    
    @property
    def genre(self) -> str:
        """Getter untuk genre"""
        return self.__genre
    
    def display_info(self) -> str:
        """
        Implementation dari abstract method display_info.
        Polymorphism - method yang sama dengan implementasi berbeda.
        """
        status = "✓ Tersedia" if self._is_available else "✗ Dipinjam"
        return f"""
{'='*60}
Tipe Item    : {self.get_item_type()}
ID           : {self.item_id}
Judul        : {self.title}
Penulis      : {self.author}
Tahun        : {self.year}
ISBN         : {self.isbn}
Halaman      : {self.pages}
Genre        : {self.genre}
Status       : {status}
{'='*60}
"""
    
    def get_item_type(self) -> str:
        """Implementation dari abstract method get_item_type"""
        return "Buku"


class Magazine(LibraryItem):
    """
    Class Magazine yang mewarisi dari LibraryItem.
    Menerapkan konsep Inheritance dan Polymorphism.
    """
    
    def __init__(self, item_id: str, title: str, publisher: str, year: int,
                 issue_number: int, month: str):
        """
        Constructor untuk Magazine
        
        Args:
            item_id: ID unik majalah
            title: Judul majalah
            publisher: Penerbit majalah
            year: Tahun publikasi
            issue_number: Nomor edisi
            month: Bulan publikasi
        """
        super().__init__(item_id, title, publisher, year)
        self.__issue_number = issue_number
        self.__month = month
    
    @property
    def issue_number(self) -> int:
        """Getter untuk issue_number"""
        return self.__issue_number
    
    @property
    def month(self) -> str:
        """Getter untuk month"""
        return self.__month
    
    def display_info(self) -> str:
        """
        Implementation dari abstract method display_info.
        Polymorphism - method yang sama dengan implementasi berbeda dari Book.
        """
        status = "✓ Tersedia" if self._is_available else "✗ Dipinjam"
        return f"""
{'='*60}
Tipe Item    : {self.get_item_type()}
ID           : {self.item_id}
Judul        : {self.title}
Penerbit     : {self.author}
Tahun        : {self.year}
Edisi        : #{self.issue_number}
Bulan        : {self.month}
Status       : {status}
{'='*60}
"""
    
    def get_item_type(self) -> str:
        """Implementation dari abstract method get_item_type"""
        return "Majalah"


class Library:
    """
    Class Library untuk mengelola koleksi item perpustakaan.
    Menerapkan konsep Encapsulation dan Composition.
    """
    
    def __init__(self, name: str):
        """
        Constructor untuk Library
        
        Args:
            name: Nama perpustakaan
        """
        self.__name = name
        self.__items: List[LibraryItem] = []  # Private list (Encapsulation)
        self.__borrowed_count = 0
    
    @property
    def name(self) -> str:
        """Getter untuk name"""
        return self.__name
    
    @property
    def total_items(self) -> int:
        """Getter untuk total items"""
        return len(self.__items)
    
    @property
    def available_items(self) -> int:
        """Getter untuk jumlah item yang tersedia"""
        return sum(1 for item in self.__items if item.is_available)
    
    def add_item(self, item: LibraryItem) -> bool:
        """
        Menambahkan item ke perpustakaan.
        
        Args:
            item: LibraryItem yang akan ditambahkan
            
        Returns:
            True jika berhasil, False jika ID sudah ada
        """
        # Cek apakah ID sudah ada
        if any(existing.item_id == item.item_id for existing in self.__items):
            print(f"❌ Error: Item dengan ID {item.item_id} sudah ada!")
            return False
        
        self.__items.append(item)
        print(f"✓ Item '{item.title}' berhasil ditambahkan!")
        return True
    
    def display_all_items(self) -> None:
        """
        Menampilkan semua item di perpustakaan.
        Mendemonstrasikan Polymorphism - memanggil method yang sama pada berbagai tipe object.
        """
        if not self.__items:
            print("\n📚 Perpustakaan masih kosong.\n")
            return
        
        print(f"\n{'='*60}")
        print(f"PERPUSTAKAAN {self.name.upper()}")
        print(f"{'='*60}")
        print(f"Total Item    : {self.total_items}")
        print(f"Tersedia      : {self.available_items}")
        print(f"Dipinjam      : {self.total_items - self.available_items}")
        print(f"{'='*60}\n")
        
        # Polymorphism: memanggil display_info() pada berbagai tipe object
        for item in self.__items:
            print(item.display_info())
    
    def search_by_title(self, title: str) -> List[LibraryItem]:
        """
        Mencari item berdasarkan judul.
        
        Args:
            title: Judul yang dicari (case-insensitive, partial match)
            
        Returns:
            List of LibraryItem yang cocok
        """
        results = [
            item for item in self.__items 
            if title.lower() in item.title.lower()
        ]
        return results
    
    def search_by_id(self, item_id: str) -> Optional[LibraryItem]:
        """
        Mencari item berdasarkan ID.
        
        Args:
            item_id: ID item yang dicari
            
        Returns:
            LibraryItem jika ditemukan, None jika tidak
        """
        for item in self.__items:
            if item.item_id == item_id:
                return item
        return None
    
    def borrow_item(self, item_id: str) -> bool:
        """
        Meminjam item dari perpustakaan.
        
        Args:
            item_id: ID item yang akan dipinjam
            
        Returns:
            True jika berhasil, False jika gagal
        """
        item = self.search_by_id(item_id)
        if item is None:
            print(f"❌ Item dengan ID {item_id} tidak ditemukan!")
            return False
        
        if item.borrow():
            self.__borrowed_count += 1
            print(f"✓ Item '{item.title}' berhasil dipinjam!")
            return True
        else:
            print(f"❌ Item '{item.title}' sedang dipinjam!")
            return False
    
    def return_item(self, item_id: str) -> bool:
        """
        Mengembalikan item ke perpustakaan.
        
        Args:
            item_id: ID item yang akan dikembalikan
            
        Returns:
            True jika berhasil, False jika gagal
        """
        item = self.search_by_id(item_id)
        if item is None:
            print(f"❌ Item dengan ID {item_id} tidak ditemukan!")
            return False
        
        if not item.is_available:
            item.return_item()
            print(f"✓ Item '{item.title}' berhasil dikembalikan!")
            return True
        else:
            print(f"❌ Item '{item.title}' tidak sedang dipinjam!")
            return False


def main():
    """
    Main function untuk menjalankan program.
    Demonstrasi penggunaan semua fitur sistem perpustakaan.
    """
    # Membuat instance Library
    library = Library("Perpustakaan Kota")
    
    print("\n" + "="*60)
    print("SISTEM MANAJEMEN PERPUSTAKAAN")
    print("="*60 + "\n")
    
    # Menambahkan beberapa buku
    book1 = Book(
        "B001", 
        "Pemrograman Python untuk Pemula",
        "John Doe",
        2023,
        "978-1234567890",
        350,
        "Teknologi"
    )
    
    book2 = Book(
        "B002",
        "Data Science dengan Python",
        "Jane Smith",
        2024,
        "978-0987654321",
        420,
        "Teknologi"
    )
    
    book3 = Book(
        "B003",
        "Seni Menulis Kode Bersih",
        "Robert Martin",
        2022,
        "978-1122334455",
        280,
        "Teknologi"
    )
    
    # Menambahkan majalah
    magazine1 = Magazine(
        "M001",
        "Tech Monthly",
        "Tech Publishers",
        2024,
        12,
        "Desember"
    )
    
    magazine2 = Magazine(
        "M002",
        "Science Today",
        "Science Media",
        2024,
        11,
        "November"
    )
    
    # Menambahkan item ke perpustakaan
    print("\n📝 MENAMBAHKAN ITEM KE PERPUSTAKAAN:")
    print("-" * 60)
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)
    library.add_item(magazine1)
    library.add_item(magazine2)
    
    # Menampilkan semua item
    print("\n📚 MENAMPILKAN SEMUA ITEM:")
    library.display_all_items()
    
    # Mencari item berdasarkan judul
    print("\n🔍 MENCARI ITEM BERDASARKAN JUDUL 'Python':")
    print("-" * 60)
    search_results = library.search_by_title("Python")
    if search_results:
        for item in search_results:
            print(item.display_info())
    else:
        print("Tidak ada item yang ditemukan.")
    
    # Meminjam item
    print("\n📤 MEMINJAM ITEM:")
    print("-" * 60)
    library.borrow_item("B001")
    library.borrow_item("M001")
    
    # Mencoba meminjam item yang sudah dipinjam
    print("\n📤 MENCOBA MEMINJAM ITEM YANG SUDAH DIPINJAM:")
    print("-" * 60)
    library.borrow_item("B001")
    
    # Menampilkan status terkini
    print("\n📊 STATUS PERPUSTAKAAN SETELAH PEMINJAMAN:")
    library.display_all_items()
    
    # Mengembalikan item
    print("\n📥 MENGEMBALIKAN ITEM:")
    print("-" * 60)
    library.return_item("B001")
    
    # Mencari item berdasarkan ID
    print("\n🔍 MENCARI ITEM BERDASARKAN ID 'B002':")
    print("-" * 60)
    item = library.search_by_id("B002")
    if item:
        print(item.display_info())
    else:
        print("Item tidak ditemukan.")
    
    # Menampilkan status akhir
    print("\n📊 STATUS AKHIR PERPUSTAKAAN:")
    library.display_all_items()
    
    print("\n" + "="*60)
    print("PROGRAM SELESAI")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()