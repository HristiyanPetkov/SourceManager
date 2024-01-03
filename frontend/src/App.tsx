import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import {Navbar} from "./components/Navbar";
import {Manager} from "./components/Manager";

function App() {
    return (
        <Router>
            <Navbar/>
            <Routes>
                <Route path="/manager" element={<Manager/>}/>
            </Routes>
        </Router>
    );
}

export default App;
