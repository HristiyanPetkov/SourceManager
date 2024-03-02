import React, {useEffect} from "react";
import {KEYCLOAK_URL, KEYCLOAK_REALM, CLIENT_ID} from "../config/KeyCloakConfig";
import { API_ENDPOINTS } from "../config/config";
import axios from "axios";
import {useNavigate} from "react-router-dom";

export const LoginHandler = () => {
    const navigate = useNavigate();

    useEffect(() => {
        console.log("LoginHandler useEffect");
        const urlParams = new URLSearchParams(window.location.search);
        const code = urlParams.get('code');
        console.log("Code: ", code);
        localStorage.setItem('code', code as string);
        localStorage.setItem('refresh_token', urlParams.get('refresh_token') as string);

        if (code) {
            exchangeCodeForToken(code as string).then(r =>{
                console.log('Token exchanged successfully');
            });
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
        console.log(keyCloakToken)
        const decodedToken = JSON.parse(atob(keyCloakToken.split('.')[1]));
        console.log("Decoded Token: ", decodedToken);
        console.log("Name: ", decodedToken.name);
        console.log("Email: ", decodedToken.email);
        console.log("Organization: ", decodedToken.organization);
        console.log("Comment: ", decodedToken.comment);

        const response = await axios.post(`${API_ENDPOINTS.user}`, {
            email: decodedToken.email,
            name: decodedToken.name,
            organization: decodedToken.organization,
            comment: decodedToken.comment
        });

        console.log("User: ", response.data);

        return response.data;
    }

    return (
        <div className="pt-16">
            <h1>Logging in</h1>
        </div>
    );
}