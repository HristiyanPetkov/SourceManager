import React, {useEffect} from "react";
import {KEYCLOAK_URL, KEYCLOAK_REALM, CLIENT_ID} from "../config/KeyCloakConfig";
import { API_ENDPOINTS } from "../config/config";
import axios from "axios";
import {useNavigate} from "react-router-dom";

export const LoginHandler = () => {
    const navigate = useNavigate();

    useEffect(() => {
        const urlParams = new URLSearchParams(window.location.search);
        const code = urlParams.get('code');
        localStorage.setItem('refresh_token', urlParams.get('refresh_token') as string);

        if (code) {
            exchangeCodeForToken(code as string).then(
                () => {
                    console.log("Token exchanged");
                }
            )
        }
    }, );

    const exchangeCodeForToken = async (code: string) => {
        const response = await axios.post(`${KEYCLOAK_URL}/realms/${KEYCLOAK_REALM}/protocol/openid-connect/token`, {
            client_id: CLIENT_ID,
            grant_type: "authorization_code",
            code: code,
            redirect_uri: "http://localhost:3000/login/callback"
        }, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });

        const keyCloakToken = response.data["access_token"];

        localStorage.setItem('access_token', keyCloakToken);
        await getUser(keyCloakToken).then(r => {
            if(r) {
                navigate('/home', { state: { user: r }});
            } else {
                navigate('/login');
            }
        });
    }

    const getUser = async (keyCloakToken: string) => {
        const decodedToken = JSON.parse(atob(keyCloakToken.split('.')[1]));

        const response = await axios.post(`${API_ENDPOINTS.user}${decodedToken.email}`, {
            email: decodedToken.email,
            name: decodedToken.name,
            organization: decodedToken.organization,
            comment: decodedToken.comment
        });

        return response.data;
    }
    return (
        <div className="flex justify-center items-center h-screen text-white text-3xl">
            <h1>Login in progress...</h1>
        </div>
    );
}