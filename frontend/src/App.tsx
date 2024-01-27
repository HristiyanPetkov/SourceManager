import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import {Navbar} from "./components/Navbar";
import {Manager} from "./components/Manager";
import {Login} from "./components/Login";
import './styles/tailwind.output.css';

function App() {
    return (
        <Router>
            <Navbar/>
            <Routes>
                <Route path="/" element={<Login/>}/>
                <Route path="/login" element={<Login/>}/>
                <Route path="/home" element={<Manager/>}/>
            </Routes>
        </Router>
    );
}

export default App;
