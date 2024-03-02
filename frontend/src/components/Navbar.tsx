import React from 'react';
import { useFilter } from '../context/FilterContext';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome } from '@fortawesome/free-solid-svg-icons';
import {Logout} from "./Logout";

export const Navbar: React.FC = () => {
  const { filter, setFilter } = useFilter();

  const handleFilterChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFilter(event.target.value);
  };

  // add logout button
  return (
    <div className="fixed top-0 left-0 w-full">
      <header className="bg-dark-blue py-2">
        <div className="container mx-auto flex items-center justify-between">
          <a href="/home" className="flex items-center text-white hover:no-underline">
            <FontAwesomeIcon icon={faHome} className="w-6 h-6 m-2" />
            <h1 className="text-xl font-bold ml-2">Source Manager</h1>
          </a>

          <input
            type="text"
            placeholder="Filter hosts"
            className="border p-2 rounded-md"
            value={filter}
            onChange={handleFilterChange}
          />

          <div className="font-bold text-xl flex items-center text-white hover:no-underline mr-4">
            <Logout />
          </div>
        </div>
      </header>
    </div>
  );
};
