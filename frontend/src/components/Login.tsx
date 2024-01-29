import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export const Login = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/login`);
            const data = await response.json();

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
            <div className="bg-gray-100 p-8 rounded shadow-md w-96 flex flex-col items-center justify-center mt-40">
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
                    className="bg-blue-500 text-white font-bold py-2 px-4 rounded cursor-pointer"
                    onClick={handleLogin}
                >
                    Login
                </button>
            </div>
        </div>
    );
};
