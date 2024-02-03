import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Navbar } from './components/Navbar';
import { Manager } from './components/Manager';
import { Login } from './components/Login';
import { FilterProvider } from './context/FilterContext';
import './styles/tailwind.output.css';

function App() {
  return (
    <Router>
      <FilterProvider>
        <Navbar />
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/login" element={<Login />} />
          <Route path="/home" element={<Manager />} />
        </Routes>
      </FilterProvider>
    </Router>
  );
}

export default App;
