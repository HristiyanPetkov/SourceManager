import {CLIENT_ID, KEYCLOAK_REALM, KEYCLOAK_URL} from "../config/KeyCloakConfig";
import {faSignOut, faUser} from "@fortawesome/free-solid-svg-icons";
import React from "react";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

export const UserActions = () => {

    const logout = async () => {
        const logout_url = `${KEYCLOAK_URL}/realms/${KEYCLOAK_REALM}/protocol/openid-connect/logout?post_logout_redirect_uri=http://localhost:3000/login&client_id=${CLIENT_ID}`;

        window.location.href = (logout_url);
    }

    const redirectToProfile = () => {
        window.location.href = `${KEYCLOAK_URL}/realms/${KEYCLOAK_REALM}/protocol/openid-connect/auth?client_id=account-console&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Frealms%2FSourceManager%2Faccount%2F%23%2F&state=7eff8c69-e9cf-45a1-b511-c7957e20e7fa&response_mode=fragment&response_type=code&scope=openid&nonce=f4c4f839-9e1d-4c60-8a39-11f231528166&code_challenge=YeedSPlKVVOwHTobiWBM68E9za2ZxHj5ea2JJakoxqg&code_challenge_method=S256`;    }

    return (
        <div className="flex items-center m-2">
            <div className="mr-4">
                <button className="text-white hover:no-underline" onClick={redirectToProfile}>
                    <FontAwesomeIcon className="w-6 h-6" icon={faUser}/>
                </button>
            </div>
            <div>
                <button className="text-white hover:no-underline" onClick={logout}>
                    <FontAwesomeIcon className="w-6 h-6" icon={faSignOut}/>
                </button>
            </div>
        </div>
    );
}