import React, { useState, useEffect } from "react";
import "./activeContent.css";
import { Hosts } from "./Hosts";
import { AddHost } from "./AddHost";

export const HostSelector = () => {
  const [activeButton, setActiveButton] = useState<string>("");
  const [activeType, setActiveType] = useState<string>("ips");
  const [reloadHosts, setReloadHosts] = useState<boolean>(false);

  const handleButtonClick = (buttonId: string) => {
    setActiveButton(buttonId);
    if (buttonId === "button1") {
      setActiveType("ips");
    } else if (buttonId === "button2") {
      setActiveType("ip_ranges");
    } else if (buttonId === "button3") {
      setActiveType("domains");
    }
    setReloadHosts(false);
  };

  const handleAddHostSuccess = () => {
    console.log("Host added successfully");
    setReloadHosts(true);
  };

  useEffect(() => {
    setReloadHosts(false);
  }, [activeType]);

  return (
    <div>
      <div id="buttonContainer" className="flex space-x-4 mb-4">
        <button
          onClick={() => handleButtonClick("button1")}
          className={`bg-dark-blue hover:bg-button-action text-white py-2 px-4 rounded ${
            activeButton === "button1" && "animate-pulse"
          }`}
        >
          Ip host
        </button>
        <button
          onClick={() => handleButtonClick("button2")}
          className={`bg-dark-blue hover:bg-button-action text-white py-2 px-4 rounded ${
            activeButton === "button2" && "animate-pulse"
          }`}
        >
          Ip range
        </button>
        <button
          onClick={() => handleButtonClick("button3")}
          className={`bg-dark-blue hover:bg-button-action text-white py-2 px-4 rounded ${
            activeButton === "button3" && "animate-pulse"
          }`}
        >
          Domain host
        </button>
      </div>

      <div
        id="content1"
        className={activeButton === "button1" ? "content active" : "content"}
      />
      <div
        id="content2"
        className={activeButton === "button2" ? "content active" : "content"}
      />
      <div
        id="content3"
        className={activeButton === "button3" ? "content active" : "content"}
      />

      <Hosts hostType={activeType} reload={reloadHosts} />
      <AddHost onSuccess={handleAddHostSuccess} />
    </div>
  );
};
