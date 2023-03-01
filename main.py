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
    positions = []

    i = 0

    all_actions = []

    while True:
        # try:
        #     print("INDEXING - ", i)
        #     n = dg.next(i)

        #     execute = brain.calculate(capital, n, positions)
        #     capital, executed, positions = executioner.trade(execute, capital, positions)

        #     for j in executed:
        #         all_actions.append(j)
        # except:
        #     break

        # print("INDEXING - ", i)
        n = dg.next(i, stocks_data)

        zero_data = np.zeros(shape=(10,10))
        dummydf = pandas.DataFrame()

        if type(n) != type(dummydf):
            break

        execute = brain.calculate(capital, n, positions)
        capital, executed, positions = executioner.trade(execute, capital, positions)

        for j in executed:
            all_actions.append(j)

        i+=1

    eval = capital
    for i in positions:
        eval += i.buy_val

    print(eval)

    # f = open('writing/actions' + t + '.csv', 'w')
    # f.close()

    # writing to csv file
    with open('writing/actions' + t + '.csv', 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerows(all_actions)

    #WRITING STATS
    # sw.write_stats()

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
