import axios from "axios";

let getWalletBalanceAPI = import.meta.env.VITE_GET_WALLET_BALANCE
async function getWalletBalance(): Promise<number> {
    // TODO: call backend to get wallet balance
    const response = await axios.get(getWalletBalanceAPI);
    return response.data.balance as number;
}

function calculateSize(walletBalance:number, pct:number, leverage: number): number {
    let capital = walletBalance * (pct / 100);
    let size = capital * leverage;
    return size;
}

export { getWalletBalance, calculateSize }