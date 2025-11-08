import { renderHook, act } from "@testing-library/react";
import { useLocalStorage } from "../hooks/useLocalStorage";

test("useLocalStorage menyimpan dan mengambil data", () => {
  const { result } = renderHook(() => useLocalStorage("test", []));
  act(() => result.current[1]([{ title: "Test Book" }]));
  expect(result.current[0][0].title).toBe("Test Book");
});
