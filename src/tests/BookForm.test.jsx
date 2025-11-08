import { render, screen, fireEvent } from "@testing-library/react";
import { BookProvider } from "../context/BookContext";
import BookForm from "../components/BookForm/BookForm";

test("Form menampilkan error saat input kosong", () => {
  render(
    <BookProvider>
      <BookForm />
    </BookProvider>
  );
  fireEvent.click(screen.getByText(/Tambah/i));
  expect(screen.getByText(/wajib diisi/i)).toBeInTheDocument();
});
