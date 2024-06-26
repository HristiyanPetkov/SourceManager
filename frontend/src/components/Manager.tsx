import React, { useState, useEffect } from "react";
import "./activeContent.css";
import { Hosts } from "./Hosts";
import { AddHost } from "./AddHost";
import {useLocation} from "react-router-dom";
import {CustomButton} from "./CutomButton";

interface User {
    id: number,
    name: string,
    email: string,
    comment: string,
    organization_id: number,
    organization_name: string,
}

export const Manager = () => {
    const location = useLocation();
    const user: User = (location.state as any)?.user;
    const [activeButton, setActiveButton] = useState<string>("button1");
    const [activeType, setActiveType] = useState<string>("ip");
    const [reloadHosts, setReloadHosts] = useState<boolean>(false);

    const handleButtonClick = (buttonId: string) => {
      setActiveButton(buttonId);
      if (buttonId === "button1") {
        setActiveType("ip");
      } else if (buttonId === "button2") {
        setActiveType("ip_range");
      } else if (buttonId === "button3") {
        setActiveType("domain");
      }
      setReloadHosts(false);
    };

    const handleGetHostsSuccess = () => {
      console.log("Hosts fetched successfully");
      setReloadHosts(false);
    }

    const handleAddHostSuccess = () => {
      console.log("Host added successfully");
      setReloadHosts(true);
    };

    useEffect(() => {
      setReloadHosts(false);
    }, [activeType]);

    return (
        <div className="flex flex-col items-center justify-center pt-16 text-xl">
            {
                user && (
                    <>
                    <p className="text-5xl font-bold">{user.organization_name}</p>
                    <p className="text-3xl">{user.name}</p>
                    <p className="text-3xl mb-2">{user.email}</p>
                    </>
                )
            }
            <div>
                <AddHost userId={user.id} organizationId={user.organization_id} onSuccess={handleAddHostSuccess} />
                <div id="buttonContainer" className="flex space-x-4 mb-4 justify-center">
                    <CustomButton onClick={() => handleButtonClick("button1")}>Ip host</CustomButton>
                    <CustomButton onClick={() => handleButtonClick("button2")}>Ip range</CustomButton>
                    <CustomButton onClick={() => handleButtonClick("button3")}>Domain host</CustomButton>
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

                <Hosts organizationId={user.organization_id} hostType={activeType} reload={reloadHosts} onSuccess={handleGetHostsSuccess} />
            </div>
        </div>
    );
};
