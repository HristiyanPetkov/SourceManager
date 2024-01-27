import React from 'react';
import { useLocation } from 'react-router-dom';
import { HostSelector } from "./HostSelector";

interface Organization {
    name: string;
}

export const Manager = () => {
    const location = useLocation();
    const organization: Organization = (location.state as any)?.organization;

    return (
        <div className="flex flex-col items-center justify-center mt-8 mb-8 text-3xl">
            {
                organization &&
                <p className="text-6xl font-bold mb-8">{organization.name}</p>
            }
            <HostSelector />
        </div>
    );
};
