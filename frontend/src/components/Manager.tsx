import React from 'react';
import { useLocation } from 'react-router-dom';
import {HostSelector} from "./HostSelector";

interface Organization {
    name: string;
    sources: string[];
    mail: string;
}

export const Manager = () => {
    const location = useLocation();
    const organization: Organization = (location.state as any)?.organization;

    return (
        <div>
            {
                organization &&
                <p>{organization.name}</p> &&
                <p>{organization.mail}</p>
            }
            <HostSelector />

        </div>
    );
}