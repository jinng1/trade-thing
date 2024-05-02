import { NavLink } from "react-router-dom";
import Home from "../pages/Home";
import Calculator from "../pages/Calculator";
import TradeJournal from "../pages/TradeJournal";
import TradeAssist from "../pages/TradeAssist";

function Navbar() {
  return (
    <div>
      <ul>
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        <li>
          <NavLink to="/calculator">Calculator</NavLink>
        </li>
        <li>
          <NavLink to="/tradejournal">Trade Journal</NavLink>
        </li>
        <li>
          <NavLink to="/tradeassist">Trade Assist</NavLink>
        </li>
      </ul>
    </div>
  );
}

export default Navbar;
