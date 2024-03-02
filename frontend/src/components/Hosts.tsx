import React, { useEffect, useState, useCallback } from 'react';
import axios from 'axios';
import { useFilter } from '../context/FilterContext';
import { API_ENDPOINTS } from "../config/config";

interface Host {
  id: number;
  value: string;
  type: string;
  comment: string;
}

interface HostsProps {
  organizationId: number;
  hostType: string;
  reload: boolean;
  onSuccess: () => void;
}

export const Hosts: React.FC<HostsProps> = ({ organizationId, hostType, reload, onSuccess}) => {
  const [hosts, setHosts] = useState<Host[]>([]);
  const [expandedHostId, setExpandedHostId] = useState<number | null>(null);
  const { filter} = useFilter();

  const fetchData = useCallback(async () => {
    try {
      if (hostType) {
        const response = await axios.get(API_ENDPOINTS.sources + hostType + '/' + organizationId);
        setHosts(response.data);
      }
      onSuccess();
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }, [organizationId, hostType, onSuccess]);

  useEffect(() => {
    fetchData().then(r => console.log('Hosts fetched successfully'));
  }, [hostType, reload, fetchData, onSuccess]);

  const handleDelete = async (hostId: number) => {
    try {
      await axios.delete(API_ENDPOINTS.sources + hostId);
      console.log('Host deleted successfully');
      fetchData();
    } catch (error) {
      console.error('Error deleting host:', error);
    }
  };

  const toggleExpand = (hostId: number) => {
    setExpandedHostId((prevId) => (prevId === hostId ? null : hostId));
  };

  const filteredHosts = hosts.filter((host) => host.value.includes(filter));

  return (
    <div>
      {filteredHosts.map((host) => (
        <div
          key={host.id}
          className={`bg-light-blue p-4 rounded-lg mb-4 cursor-pointer flex justify-between items-center overflow-hidden transition-height ${
            expandedHostId === host.id ? 'h-auto' : 'h-16'
          }`}
          onClick={() => toggleExpand(host.id)}
        >
          <div>
            <p className="mb-2">{host.value}</p>
            {expandedHostId === host.id && (
              <p className="text-gray-500 italic">{host.comment}</p>
            )}
          </div>
          {expandedHostId === host.id && (
            <button
              onClick={() => handleDelete(host.id)}
              className="bg-red-500 text-white py-2 px-4 rounded"
            >
              Delete
            </button>
          )}
        </div>
      ))}
    </div>
  );
};
