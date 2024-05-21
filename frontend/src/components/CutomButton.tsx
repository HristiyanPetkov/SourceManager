import React from "react";

type CustomButtonProps = {
  onClick: () => void;
  children: React.ReactNode;
};

export const CustomButton: React.FC<CustomButtonProps> = ({ onClick, children }) => {
  return (
    <button className="bg-dark-blue hover:bg-button-action text-white py-2 px-4 rounded-lg" onClick={onClick}>
      {children}
    </button>
  );
}
