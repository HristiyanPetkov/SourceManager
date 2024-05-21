import { useFilter } from '../context/FilterContext';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome } from '@fortawesome/free-solid-svg-icons';
import { UserActions } from "./UserActions";
import React from "react";

export const Navbar: React.FC = () => {
  const { filter, setFilter } = useFilter();

  const handleFilterChange = (event: React.ChangeEvent<HTMLInputElement>) => {
      setFilter(event.target.value);
  };

  return (
    <div className="fixed top-0 left-0 w-full">
        <nav>
          <header className="bg-dark-blue py-2">
              <div className="container mx-auto flex items-center justify-between">
                  <a href="/home" className="flex items-center text-white hover:no-underline">
                      <FontAwesomeIcon icon={faHome} className="w-6 h-6 m-2"/>
                      <h1 className="text-xl font-bold ml-2">Source Manager</h1>
                  </a>

                  <input
                      id="filter"
                      type="text"
                      placeholder="Filter hosts"
                      className="border p-2 rounded-md"
                      value={filter}
                      onChange={handleFilterChange}
                  />

                  <UserActions />
              </div>
          </header>
        </nav>
    </div>
  );
};
