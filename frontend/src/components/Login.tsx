import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { API_ENDPOINTS } from "../config/config";
import axios from 'axios';

export const Login = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        try {
            const response = await axios.post(API_ENDPOINTS.login, {
                                                email: email,
                                                password: password,
                                              });
            const data = response.data;

            if (data) {
                navigate('/home', { state: { user: data } });
            }
        } catch (error) {
            console.error('Login failed:', error);
            navigate('/login');
        }
    };

    return (
        <div className="flex items-center justify-center h-full">
            <div className="bg-light-blue p-8 rounded shadow-md w-96 flex flex-col items-center justify-center mt-40">
                <h2 className="text-3xl font-bold mb-4">Login</h2>
                <input
                    className="mb-4 p-2 border border-gray-300 rounded"
                    type="text"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    className="mb-4 p-2 border border-gray-300 rounded"
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button
                    className="bg-dark-blue hover:bg-button-action text-white font-bold py-2 px-4 rounded cursor-pointer"
                    onClick={handleLogin}
                >
                    Login
                </button>
            </div>
        </div>
    );
};
