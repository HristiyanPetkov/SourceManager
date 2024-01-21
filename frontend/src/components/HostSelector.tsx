import {useState} from "react";
import "./activeContent.css";
import {Hosts} from "./Hosts";
import {AddHost} from "./AddHost";

export const HostSelector = () => {

    const [activeButton, setActiveButton] = useState<string>('button1');
    const [activeType, setActiveType] = useState<string>('ips');

    const handleButtonClick = (buttonId: string) => {
        setActiveButton(buttonId);
        if (buttonId === 'button1') {
            setActiveType('ips');
        } else if (buttonId === 'button2') {
            setActiveType('ip_ranges');
        } else if (buttonId === 'button3') {
            setActiveType('domains');
        }
    };

    const handleAddHostSuccess = () => {
        console.log('Host added successfully');
    };

    return (
        <div>
          <div id="buttonContainer">
            <button onClick={() => handleButtonClick('button1')}>Ip host</button>
            <button onClick={() => handleButtonClick('button2')}>Ip range</button>
            <button onClick={() => handleButtonClick('button3')}>Domain host</button>
          </div>

          <div id="content1" className={activeButton === 'button1' ? 'content active' : 'content'}/>
          <div id="content2" className={activeButton === 'button2' ? 'content active' : 'content'}/>
          <div id="content3" className={activeButton === 'button3' ? 'content active' : 'content'}/>

            <Hosts hostType={activeType}/>
            <AddHost onSuccess={handleAddHostSuccess}/>
        </div>
    );
};
