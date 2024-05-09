class Trade:
    def __init__(self, symbol, datetime, direction, entries, exit, size, pnl):
        self.symbol = symbol
        self.datetime = datetime
        self.direction = direction
        self.entries = entries
        self.exit = exit
        self.size = size
        self.pnl = pnl
