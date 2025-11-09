import React, { useState } from "react";
import BookForm from "../../components/BookForm/BookForm";
import BookList from "../../components/BookList/BookList";
import BookFilter from "../../components/BookFilter/BookFilter";

export default function Home() {
  const [filter, setFilter] = useState("all");
  const [search, setSearch] = useState("");

  return (
    <div className="home-container">
      <h2 className="section-title">📖 Manage Your Books</h2>

      <div className="book-section">
        <BookForm />
      </div>

      <div className="book-section">
        <BookFilter 
          filter={filter} 
          setFilter={setFilter} 
          search={search} 
          setSearch={setSearch} 
        />
      </div>

      <div className="book-section">
        <BookList filter={filter} search={search} />
      </div>
    </div>
  );
}
