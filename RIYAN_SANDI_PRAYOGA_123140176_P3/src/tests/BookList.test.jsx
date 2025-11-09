import { render, screen } from "@testing-library/react";
import { BookContext } from "../context/BookContext";
import BookList from "../components/BookList/BookList";

test("Menampilkan pesan kosong jika tidak ada buku", () => {
  render(
    <BookContext.Provider value={{ books: [], deleteBook: jest.fn() }}>
      <BookList filter="all" search="" />
    </BookContext.Provider>
  );
  expect(screen.getByText(/Tidak ada buku/i)).toBeInTheDocument();
});
