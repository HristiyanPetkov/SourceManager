import {useState} from "react";
import "./activeContent.css";
import {IPHosts} from "./IPHosts";
import {IPRangeHosts} from "./IPRangeHosts";
import {DomainHosts} from "./DomainHosts";

export const HostSelector = () => {

    const [activeButton, setActiveButton] = useState<string>('button1');

    const handleButtonClick = (buttonId: string) => {
        setActiveButton(buttonId);
    };

    return (
        <div>
          <div id="buttonContainer">
            <button onClick={() => handleButtonClick('button1')}>Ip host</button>
            <button onClick={() => handleButtonClick('button2')}>Ip range</button>
            <button onClick={() => handleButtonClick('button3')}>Domain host</button>
          </div>

          <div id="content1" className={activeButton === 'button1' ? 'content active' : 'content'}>
            <IPHosts />
          </div>

          <div id="content2" className={activeButton === 'button2' ? 'content active' : 'content'}>
            <IPRangeHosts />
          </div>

          <div id="content3" className={activeButton === 'button3' ? 'content active' : 'content'}>
            <DomainHosts />
          </div>
        </div>
    );
};
