import React, { createContext, useState, useEffect } from "react";
import { useLocalStorage } from "../hooks/useLocalStorage";

export const BookContext = createContext();

export const BookProvider = ({ children }) => {
  const [books, setBooks] = useLocalStorage("books", []);

  const addBook = (book) => setBooks([...books, book]);
  const updateBook = (updated) =>
    setBooks(books.map((b) => (b.id === updated.id ? updated : b)));
  const deleteBook = (id) => setBooks(books.filter((b) => b.id !== id));

  return (
    <BookContext.Provider value={{ books, addBook, updateBook, deleteBook }}>
      {children}
    </BookContext.Provider>
  );
};
