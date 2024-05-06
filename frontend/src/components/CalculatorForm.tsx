import React, { useState, useEffect } from "react";
import { calculateSize, getWalletBalance } from "../utils/calculatorUtils";

export default function CalculatorForm() {
  const [balance] = useState(getWalletBalance());
  const [formData, setFormData] = useState({
    // Initial form data values
    balance: balance,
    leverage: 50,
    entry: 0.5,
    dca1: 1,
    dca2: 1.5,
  });

  const [entrySize, setEntrySize] = useState(0);
  const [dca1Size, setDca1Size] = useState(0);
  const [dca2Size, setDca2Size] = useState(0);

  function handleInputChange(event: any) {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  }

  useEffect(() => {
    setEntrySize(
      calculateSize(formData.balance, formData.entry, formData.leverage)
    );
    setDca1Size(
      calculateSize(formData.balance, formData.dca1, formData.leverage)
    );
    setDca2Size(
      calculateSize(formData.balance, formData.dca2, formData.leverage)
    );
  });

  return (
    <div>
      <form>
        <label htmlFor="balance">Wallet Balance</label>
        <input
          type="number"
          name="balance"
          value={formData.balance}
          onChange={handleInputChange}
        />
        <label htmlFor="leverage">Leverage</label>
        <input
          type="number"
          name="leverage"
          value={formData.leverage}
          onChange={handleInputChange}
        />
        <label htmlFor="entry">entry</label>
        <input
          type="number"
          name="entry"
          value={formData.entry}
          onChange={handleInputChange}
        />
        <label htmlFor="dca1">DCA 1</label>
        <input
          type="number"
          name="dca1"
          value={formData.dca1}
          onChange={handleInputChange}
        />
        <label htmlFor="dca2">DCA 2</label>
        <input
          type="number"
          name="dca2"
          value={formData.dca2}
          onChange={handleInputChange}
        />
      </form>
      <div>
        <ul>
          <li>Entry Size: {entrySize}</li>
          <li>DCA 1 Size: {dca1Size}</li>
          <li>DCA 2 Size: {dca2Size}</li>
        </ul>
      </div>
    </div>
  );
}
