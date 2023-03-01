class position(object):
    def __init__(self, ticker, qty, buy_val):
        self.ticker = ticker
        self.qty = qty
        self.buy_val = buy_val

    def show(self):
        print(self.ticker, self.qty,
              self.buy_val)

def trade(execute, capital, positions):
    positions = positions
    executed = []
    capital = capital
    transaction_cost = 0
    ctr = 0
    for e in execute:
        # print("EXECUTING: - ", ctr)
        if e.buy:
            capital -= e.buy_val
            capital -= transaction_cost
            new_pos = position(e.ticker, e.qty, e.buy_val)
            positions.append(new_pos)
            # print("BOUGHT -", e.ticker, " -", e.buy_val)
            executed.append(('BOUGHT', e.ticker, e.buy_val, capital, e.date))
        elif e.sell:
            capital += e.sell_val
            capital -= transaction_cost
            positions.pop()
            # print("SOLD -", e.ticker, " -", e.sell_val)
            executed.append(('SOLD', e.ticker, e.sell_val, capital, e.date))
        ctr += 1

    return capital, executed, positions

