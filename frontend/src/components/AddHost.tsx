import React, { useState } from 'react';
import axios from 'axios';

interface AddHostFormProps {
  onSuccess: () => void;
}

export const AddHost: React.FC<AddHostFormProps> = ({ onSuccess }) => {
  const [hostType, setHostType] = useState<string>('ip');
  const [hostValue, setHostValue] = useState<string>('');
  const [comment, setComment] = useState<string>('');

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      await axios.post('http://127.0.0.1:8000/sources/', {
        type: hostType,
        value: hostValue,
        comment: comment,
        organization_id: 1,
      });

      setHostType('ip');
      setHostValue('');
      setComment('');
      onSuccess();
    } catch (error) {
      console.error('Error adding host:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Host Type:
        <select value={hostType} onChange={(e) => setHostType(e.target.value)}>
          <option value="ip">IP</option>
          <option value="ip_range">IP Range</option>
          <option value="domain">Domain</option>
        </select>
      </label>

      <label>
        Host Value:
        <input type="text" value={hostValue} onChange={(e) => setHostValue(e.target.value)} />
      </label>

        <label>
            Comment:
            <input type="text" value={comment} onChange={(e) => setComment(e.target.value)} />
        </label>

      <button type="submit">Add Host</button>
    </form>
  );
};
