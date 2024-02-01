import React from 'react';
import { useLocation } from 'react-router-dom';
import { HostSelector } from "./HostSelector";

interface User {
    name: string,
    email: string,
    comment: string,
    phone: string,
    organization_id: number,
    organization_name: string,
}

export const Manager = () => {
    const location = useLocation();
    const user: User = (location.state as any)?.user;

    console.log(user);

    return (
        <div className="flex flex-col items-center justify-center mt-2 mb-8 text-3xl">
            {
                user && (
                    <>
                    <p className="text-6xl font-bold">{user.organization_name}</p>
                    <p className="text-4xl">{user.name}</p>
                    <p className="text-4xl mb-2">{user.email}</p>
                    </>
                )
            }
            <HostSelector />
        </div>
    );
};
