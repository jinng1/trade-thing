/*
TODO:
- wallet balance

- entries and dca sizes (to input to the trades)
- stop loss?
*/

function getWalletBalance(): number {
    // TODO: call backend to get wallet balance
    return 350;
}

function calculateSize(walletBalance:number, pct:number, leverage: number): number {
    let capital = walletBalance * (pct / 100);
    let size = capital * leverage;
    return size;
}

export { getWalletBalance, calculateSize }