import React, { useContext } from "react";
import { BookContext } from "../../context/BookContext";

export default function BookList({ filter, search }) {
  const { books, deleteBook } = useContext(BookContext);

  const filtered = books.filter((b) => {
    const matchesStatus = filter === "all" || b.status === filter;
    const matchesSearch = b.title.toLowerCase().includes(search.toLowerCase());
    return matchesStatus && matchesSearch;
  });

  return (
    <div>
      <h3>Daftar Buku ({filtered.length})</h3>
      {filtered.length === 0 && <p>Tidak ada buku ditemukan.</p>}
      {filtered.map((book) => (
        <div key={book.id} className="book-card">
          <strong>{book.title}</strong> <br />
          <small>{book.author}</small> <br />
          <small>Status: {book.status}</small> <br />
          <button onClick={() => deleteBook(book.id)}>Hapus</button>
        </div>
      ))}
    </div>
  );
}
