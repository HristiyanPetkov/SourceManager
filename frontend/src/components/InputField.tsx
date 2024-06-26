import React from "react";

interface InputProps {
    label: string;
    value: string;
    placeholder?: string;
    setValue: (value: string) => void;
}

export const InputField: React.FC<InputProps> = ({ label, value, placeholder, setValue }) => {
    return (
        <div className="mb-4">
            <label className="block">
                {label}:
                <input
                    type="text"
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                    placeholder={placeholder}
                    className="border p-2 ml-2 rounded-lg"
                />
            </label>
        </div>
    )
}