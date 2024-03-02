import {useEffect} from "react";
import {CLIENT_ID, KEYCLOAK_REALM, KEYCLOAK_URL} from "../config/KeyCloakConfig";

export const Login = () => {

    useEffect(() => {
        const authorization_url = `${KEYCLOAK_URL}/realms/${KEYCLOAK_REALM}/protocol/openid-connect/auth?response_type=code&client_id=${CLIENT_ID}&redirect_uri=http://localhost:3000/login/callback`
        window.location.href = (authorization_url);
    }, []);

    return (
        <div></div>
    );
}