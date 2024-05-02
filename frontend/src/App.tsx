import { useState } from "react";
import { Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home";
import Calculator from "./pages/Calculator";
import TradeJournal from "./pages/TradeJournal";
import TradeAssist from "./pages/TradeAssist";
import Navbar from "./components/Navbar";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/calculator" element={<Calculator />} />
        <Route path="/tradejournal" element={<TradeJournal />} />
        <Route path="/tradeassist" element={<TradeAssist />} />
      </Routes>
      <Navbar />
    </div>
  );
}

export default App;
