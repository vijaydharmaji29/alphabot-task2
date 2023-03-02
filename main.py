import brain
import data_giver as dg
import executioner
import csv
# import stats_writer as sw
import os
import pandas
import data_collection as dc
import numpy as np

def run(t, stocks_data):
    
    capital = 10000000
    icap = capital
    positions = []

    i = 0

    date_ctr = 0
    date_checking = 0
    max_trades_per_day = 5

    percent = 1

    all_actions = []

    while True:
        n = dg.next(i, stocks_data)

        zero_data = np.zeros(shape=(10,10))
        dummydf = pandas.DataFrame()

        if type(n) != type(dummydf):
            break

        session_date = n.iloc[0]['date_actual']
    
        if date_checking != session_date:
            date_checking = session_date
            date_ctr = 0
        

        execute, trade_type, eod = brain.calculate(capital, n, positions)

        if eod or date_ctr < max_trades_per_day*2:
            capital, executed, positions = executioner.trade(execute, capital, positions)

            if len(execute) > 0:

                # print('TRADE DATE: ', session_date)
                # print('TRADE NUMBER: ', date_ctr)

                date_ctr += 1

                if execute[0].sell and trade_type:
                    percent -= .2
                    capital*percent

                    if capital < icap*.2:
                        capital = icap*.2

                elif execute[0].sell and  not trade_type:
                    capital = icap

            for j in executed:
                all_actions.append(j)

        i+=1

    eval = capital
    for i in positions:
        eval += i.buy_val

    print(eval)


    # writing to csv file
    with open('writing/actions' + t + '.csv', 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerows(all_actions)

if __name__ == '__main__':
    ts = os.listdir('data2/')
    tickers = []

    for t in ts:
        tickers.append(t[:-4])


    for t in tickers:
        stocks_data = {}
        ticker_data = dc.get_data(t)
        stocks_data[t] = ticker_data
        print("RUNNING FOR: ", t, tickers.index(t))
        run(t, stocks_data)

    # stocks_data = {}
    # ticker_data = dc.get_data(tickers[0])
    # stocks_data[tickers[0]] = ticker_data
    # print("RUNNING FOR: ", tickers[0], tickers.index(tickers[0]))
    # run(t, stocks_data)

    # print(tickers)
