import {useEffect} from "react";
import {CLIENT_ID, KEYCLOAK_REALM, KEYCLOAK_URL} from "../config/KeyCloakConfig";

export const Login = () => {

    useEffect(() => {
        const base_url = window.location.origin;
        const callback_uri = `${base_url}/login/callback`;
        window.location.href = `${KEYCLOAK_URL}/realms/${KEYCLOAK_REALM}/protocol/openid-connect/auth?response_type=code&client_id=${CLIENT_ID}&redirect_uri=${encodeURIComponent(callback_uri)}`;
    }, []);

    return (
        <div></div>
    );
}