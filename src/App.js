import React from "react";
import { BrowserRouter as Router, Routes, Route, NavLink } from "react-router-dom";
import Home from "./pages/Home/Home";
import Stats from "./pages/Stats/Stats";
import { BookProvider } from "./context/BookContext";

function App() {
  return (
    <BookProvider>
      <Router>
        <div className="app">
          <nav className="navbar">
            <h2>📚 sandi library Manager</h2>
            <div className="nav-links">
              <NavLink to="/" end>Home</NavLink>
              <NavLink to="/stats">Stats</NavLink>
            </div>
          </nav>

          <div className="container">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/stats" element={<Stats />} />
            </Routes>
          </div>
        </div>
      </Router>
    </BookProvider>
  );
}

export default App;
