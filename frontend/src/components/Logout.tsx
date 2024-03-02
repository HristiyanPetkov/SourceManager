import {KEYCLOAK_REALM, KEYCLOAK_URL} from "../config/KeyCloakConfig";

export const Logout = () => {

    const logout = async () => {
        const logout_url = `${KEYCLOAK_URL}/realms/${KEYCLOAK_REALM}/protocol/openid-connect/logout`;

        window.location.href = (logout_url);
    }

    return (
        <div>
            <button className="text-white hover:no-underline" onClick={logout}>Logout</button>
        </div>
    );
}