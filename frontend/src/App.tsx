import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Navbar } from './components/Navbar';
import { Manager } from './components/Manager';
import { FilterProvider } from './context/FilterContext';
import './styles/tailwind.output.css';
import {Login} from "./components/Login";
import {LoginHandler} from "./components/LoginHandler";

function App() {
  return (
    <Router>
      <FilterProvider>
        <Navbar />
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/login" element={<Login />} />
          <Route path="/login/callback" element={<LoginHandler />} />
          <Route path="/home" element={<Manager />} />
        </Routes>
      </FilterProvider>
    </Router>
  );
}

export default App;
