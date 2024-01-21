import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Host {
  id: number;
  value: string;
  type: string;
}

interface HostsProps {
  hostType: string;
}

export const Hosts: React.FC<HostsProps> = ({ hostType }) => {
  const [hosts, setHosts] = useState<Host[]>([]);

  const fetchData = async () => {
    try {
      if (hostType) {
        const response = await axios.get(`http://127.0.0.1:8000/sources/${hostType}/`);
        setHosts(response.data);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    fetchData().then(r => console.log(r));
  }, [hostType]);

  const handleDelete = async (hostId: number) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/sources/${hostId}/`);

      fetchData().then(r => console.log(r));
      console.log('Host deleted successfully');
    } catch (error) {
      console.error('Error deleting host:', error);
    }
  };

  return (
    <div>
      <h1>Hosts</h1>
      <ul>
        {hosts.map((host) => (
          <li key={host.id}>
            {host.value}
            <button onClick={() => handleDelete(host.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};
