import { render, screen, fireEvent } from "@testing-library/react";
import BookFilter from "../components/BookFilter/BookFilter";

test("Filter dapat diubah", () => {
  const setFilter = jest.fn();
  render(<BookFilter filter="all" setFilter={setFilter} search="" setSearch={() => {}} />);
  fireEvent.change(screen.getByDisplayValue("Semua"), { target: { value: "baca" } });
  expect(setFilter).toHaveBeenCalledWith("baca");
});
