import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome } from '@fortawesome/free-solid-svg-icons';

export const Navbar = () => {
  return (
    <div>
      <header className="bg-dark-blue py-2">
        <div className="container mx-auto flex items-center justify-between">
          <a href="/home" className="flex items-center text-white hover:no-underline">
            <FontAwesomeIcon icon={faHome} className="w-6 h-6 m-2" />
            <h1 className="text-xl font-bold ml-2">Source Manager</h1>
          </a>
        </div>
      </header>
    </div>
  );
};