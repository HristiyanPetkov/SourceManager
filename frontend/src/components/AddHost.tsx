import React, { useState } from 'react';
import axios from 'axios';
import {API_ENDPOINTS} from "../config/config";
import {InputField} from "./InputField";

interface AddHostFormProps {
  userId: number;
  organizationId: number;
  onSuccess: () => void;
}

export const AddHost: React.FC<AddHostFormProps> = ({ userId, organizationId, onSuccess }) => {
  const [hostType, setHostType] = useState<string>('ip');
  const [hostValue, setHostValue] = useState<string>('');
  const [comment, setComment] = useState<string>('');

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      await axios.post(API_ENDPOINTS.sources, {
        type: hostType,
        value: hostValue,
        comment: comment,
        organization_id: organizationId,
        user_id: userId,
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
    <form onSubmit={handleSubmit} className="p-4 mb-4 bg-light-blue rounded-lg">
      <div className="mb-4 rounded-lg">
        <label className="block">
          Host Type:
          <select
            value={hostType}
            onChange={(e) => setHostType(e.target.value)}
            className="border p-2 ml-2 rounded-lg"
          >
            <option value="ip">IP</option>
            <option value="ip_range">IP Range</option>
            <option value="domain">Domain</option>
          </select>
        </label>
      </div>

      <InputField label="Host Value" value={hostValue} setValue={setHostValue} />
      <InputField label="Comment (Optional)" value={comment} setValue={setComment} />

      <button type="submit" className="bg-dark-blue hover:bg-button-action text-white py-2 px-4 rounded-lg">
        Add Host
      </button>
    </form>
  );
};
