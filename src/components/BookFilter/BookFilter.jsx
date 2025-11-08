import React from "react";

export default function BookFilter({ filter, setFilter, search, setSearch }) {
  return (
    <div style={{ marginBottom: "1rem" }}>
      <label>Cari Buku: </label>
      <input
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Ketik judul..."
      />

      <label>Status: </label>
      <select value={filter} onChange={(e) => setFilter(e.target.value)}>
        <option value="all">Semua</option>
        <option value="milik">Milik</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>
    </div>
  );
}
