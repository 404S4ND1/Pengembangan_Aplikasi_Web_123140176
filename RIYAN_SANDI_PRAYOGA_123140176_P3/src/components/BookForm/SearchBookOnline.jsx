import React, { useState, useEffect } from "react";


export default function SearchBookOnline({ onSelect }) {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!query.trim()) {
      setResults([]);
      return;
    }

    const controller = new AbortController();
    const fetchBooks = async () => {
      setLoading(true);
      setError("");
      try {
        const res = await fetch(
          `https://openlibrary.org/search.json?q=${encodeURIComponent(query)}&limit=5`,
          { signal: controller.signal }
        );
        if (!res.ok) throw new Error("Gagal memuat data");
        const data = await res.json();
        setResults(data.docs || []);
      } catch (err) {
        if (err.name !== "AbortError") setError("Gagal memuat hasil pencarian");
      } finally {
        setLoading(false);
      }
    };
    fetchBooks();

    return () => controller.abort();
  }, [query]);

  return (
    <div style={{ marginBottom: "1rem" }}>
      <label>Cari Buku Online</label>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ketik judul buku..."
      />
      {loading && <div>Sedang mencari...</div>}
      {error && <div className="error">{error}</div>}
      <div style={{ maxHeight: 150, overflowY: "auto" }}>
        {results.map((b) => (
          <div
            key={b.key}
            onClick={() => {
              onSelect({
                title: b.title,
                author: b.author_name ? b.author_name[0] : "",
              });
              setQuery("");
              setResults([]);
            }}
            style={{
              cursor: "pointer",
              padding: "4px 8px",
              borderBottom: "1px solid #eee",
            }}
          >
            <strong>{b.title}</strong>{" "}
            {b.author_name && <small>oleh {b.author_name[0]}</small>}
          </div>
        ))}
      </div>
    </div>
  );
}
