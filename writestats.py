#independent program to calculate statistics
import math
from datetime import datetime
import csv
import os


#intialising variables

capital = 10000000
icap = capital
position_ticker = {}
profitable_trades = []
loss_making_trades = []
start_date = datetime.today()
end_date = datetime.today()

flag = True

max = icap
min = icap

transaction_cost = 0

f = open("all_stats.txt", "w")


def calc_drawdown():
    global max
    global min
    tval = capital
    for i in position_ticker:
        tval += position_ticker[i]

    if tval > max:
        max = tval
    if tval < min:
        min = tval

def run(filename):

    global capital, icap, position_ticker, profitable_trades, loss_making_trades, start_date, end_date, flag, max, min, transaction_cost, f

    # opening the CSV file
    with open('writing/' + filename, mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)

        # displaying the contents of the CSV file
        for row in csvFile:
            action, ticker, val, date = row[0], row[1], float(row[2]), row[-1]
            date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            if flag:
                start_date = date
                end_date = date
                flag = False

            if date > end_date:
                end_date = date

            if val == 0:
                continue

            if action == 'BOUGHT':
                position_ticker[ticker] = val
                capital -= val
            elif action == 'SOLD':
                capital += val
                trade_profit = position_ticker[ticker] - val
                profit_percentage = trade_profit*100/position_ticker[ticker]
                trade = (ticker, position_ticker[ticker], val, trade_profit, profit_percentage)
                if trade_profit > 0:
                    profitable_trades.append(trade)
                else:
                    loss_making_trades.append(trade)
                position_ticker.pop(ticker)

            calc_drawdown()
    ##calculating all stats:
    no_proftable_trades = len(profitable_trades)
    no_loss_making_trades = len(loss_making_trades)
    no_total_trades = no_loss_making_trades+no_proftable_trades
    win_rate = no_proftable_trades/no_total_trades

    total_profits = 0
    avg_profit_per_trade = 0 #only if the trade is profitable
    total_loss = 0
    avg_loss_per_trade = 0 #only if the trade is loss making

    for i in profitable_trades:
        total_profits += i[3]

    for i in loss_making_trades:
        total_loss += i[3]

    avg_loss_per_trade = total_loss/no_loss_making_trades
    avg_profit_per_trade = total_profits/no_proftable_trades

    final_val = capital

    equity = 0

    for i in position_ticker:
        equity += position_ticker[i]

    final_val += equity

    final_profit = final_val - icap - (transaction_cost*2*no_total_trades)

    dtstart = start_date
    dtend = end_date
    total_days = int((dtend - dtstart).days)

    expectancy = win_rate*avg_profit_per_trade + (1 - win_rate)*avg_loss_per_trade

    total_loss_profit_perc = 0
    for i in loss_making_trades + profitable_trades:
        total_loss_profit_perc += i[-1]

    ror = total_loss_profit_perc/no_total_trades

    max_drawdown = min - max
    max_drawdown_perc = max_drawdown*100/max

    cagr = ((math.pow(((final_profit + icap)/icap),365/total_days)) - 1)*100

    risk_reward_ratio = total_profits/total_loss

    f.write("STOCK - " + filename[7:-4] + '\n')
    f.write('BACKTEST START DATE: ' + str(start_date) + '\n')
    f.write('BACKTEST END DATE: ' + str(end_date) + '\n')
    f.write('TOTAL DAYS: ' +  str(total_days) + '\n')
    f.write('FINAL PROFIT: ' + str(final_profit) + '\n')
    f.write('TOTAL TRADES: ' + str(no_total_trades) + '\n')
    f.write('PROFITABLE TRADES: ' + str(no_proftable_trades) + '\n')
    f.write('LOSS MAKING TRADES: ' + str(no_loss_making_trades) + '\n')
    f.write('WIN RATE: ' + str(win_rate) + '\n')
    f.write('AVG PROFIT PER TRADE: ' + str(avg_profit_per_trade) + '\n')
    f.write('AVG LOSS PER TRADE: ' + str(avg_loss_per_trade) + '\n')
    f.write('RISK REWARD RATIO: ' + str(risk_reward_ratio) + '\n')
    f.write('EXPECTANCY: ' + str(expectancy) + '\n')
    f.write('AVERAGE ROR PER TRADE: (%)' + str(ror) + '\n')
    f.write('MAX DRAWDOWN: ' + str(max_drawdown) + '\n')
    f.write('MAX DRAWDOWN PERCENTAGE: ' + str(max_drawdown_perc) + '\n')
    f.write('AVG ANNUALISED RETURNS (%): ' + str(cagr) + '\n')
    f.write('\n***************************\n')

    #resting variables
    capital = 10000000
    icap = capital
    position_ticker = {}
    profitable_trades = []
    loss_making_trades = []
    start_date = datetime.today()
    end_date = datetime.today()

    flag = True

    max = icap
    min = icap

    transaction_cost = 0

if __name__ == '__main__':
    files = os.listdir('writing/')
    
    print(files)


    for i in files:
        run(i)