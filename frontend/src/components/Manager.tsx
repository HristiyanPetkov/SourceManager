import React from 'react';
import { useLocation } from 'react-router-dom';

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
            <h2>Main Page</h2>
            {organization && <p>Welcome, {organization.name}!</p>}
            {/* Render other content based on user information */}
        </div>
    );
}