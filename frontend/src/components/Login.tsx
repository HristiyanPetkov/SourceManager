import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export const Login = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');

    const handleLogin = async () => {
        try {
            // Perform GET request to the backend with username
            const response = await fetch(`http://127.0.0.1:8000/login`);
            const data = await response.json();

            // Assuming the backend returns user information
            // You can customize this logic based on your backend response
            if (data) {
                // Redirect to the main page with the user information
                navigate('/home', { state: { organization: data } });
            }
        } catch (error) {
            console.error('Login failed:', error);
            navigate('/login')
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <button onClick={handleLogin}>Login</button>
        </div>
    );
}