import React, { useState, useContext } from "react";
import { BookContext } from "../../context/BookContext";
import SearchBookOnline from "./SearchBookOnline";

export default function BookForm() {
  const { addBook } = useContext(BookContext);
  const [form, setForm] = useState({ title: "", author: "", status: "milik" });
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!form.title.trim() || !form.author.trim()) {
      setError("Judul dan Penulis wajib diisi!");
      return;
    }
    addBook({ ...form, id: Date.now() });
    setForm({ title: "", author: "", status: "milik" });
    setError("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Tambah Buku</h3>

      <label>Judul</label>
      <input
        value={form.title}
        onChange={(e) => setForm({ ...form, title: e.target.value })}
      />

      <label>Penulis</label>
      <input
        value={form.author}
        onChange={(e) => setForm({ ...form, author: e.target.value })}
      />

      {/* 🔎 Cari buku dari Open Library */}
      <SearchBookOnline onSelect={(book) => setForm((f) => ({ ...f, ...book }))} />

      <label>Status</label>
      <select
        value={form.status}
        onChange={(e) => setForm({ ...form, status: e.target.value })}
      >
        <option value="milik">Milik</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>

      {error && <div className="error">{error}</div>}

      <button type="submit">Tambah</button>
    </form>
  );
}
