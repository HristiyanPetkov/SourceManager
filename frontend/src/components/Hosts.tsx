import React, { useEffect, useState, useCallback } from 'react';
import axios from 'axios';

interface Host {
  id: number;
  value: string;
  type: string;
  comment: string;
}

interface HostsProps {
  hostType: string;
  reload: boolean;
}

export const Hosts: React.FC<HostsProps> = ({ hostType, reload }) => {
  const [hosts, setHosts] = useState<Host[]>([]);
  const [expandedHostId, setExpandedHostId] = useState<number | null>(null);

  const fetchData = useCallback(async () => {
    try {
      if (hostType) {
        const response = await axios.get(`http://127.0.0.1:8000/sources/${hostType}/`);
        setHosts(response.data);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }, [hostType]);

  useEffect(() => {
    fetchData().then(r => console.log(r));
  }, [hostType, reload, fetchData]);

  const handleDelete = async (hostId: number) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/sources/${hostId}/`);
      console.log('Host deleted successfully');
      fetchData(); // Trigger a reload after successfully deleting a host
    } catch (error) {
      console.error('Error deleting host:', error);
    }
  };

  const toggleExpand = (hostId: number) => {
    setExpandedHostId((prevId) => (prevId === hostId ? null : hostId));
  };

  return (
    <div>
      {hosts.map((host) => (
        <div
          key={host.id}
          className={`bg-light-blue p-4 rounded mb-4 cursor-pointer flex justify-between items-center overflow-hidden transition-height ${
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
