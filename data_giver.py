import os

import pandas as pd
import data_collection as dc


def next(index, stocks_data):

    # tickers = os.listdir('data2/')
    # tickers = []
    # tickers.append(t)

    # print('GETTING STOCK DATA FOR', t)

    # stocks_data = {}

    #getting data for all stocks in the timeframe
    # for t in tickers:
    #     ticker_data = dc.get_data(t)
    #     stocks_data[t] = ticker_data]
    
    n = 0
    for i in stocks_data:
        n = len(stocks_data[i])

    if index < n:
        data = {
            'symbol': [], 'close':[], 'filt': [], 'close_dif': [], 'direction':[], 'pivot': [],'date': [], 'time': []
        }

        for t in stocks_data:
            symbol = stocks_data[t].iloc[index].symbol
            close = stocks_data[t].iloc[index]['close']
            filt = stocks_data[t].iloc[index]['filt']
            close_dif = stocks_data[t].iloc[index]['close_dif']
            direction = stocks_data[t].iloc[index]['direction']
            pivot = stocks_data[t].iloc[index]['pivot']
            date = stocks_data[t].iloc[index]['datetime']
            time = stocks_data[t].iloc[index]['time']

            data['symbol'].append(symbol)
            data['close'].append(close)
            data['filt'].append(filt)
            data['close_dif'].append(close_dif)
            data['direction'].append(direction)
            data['pivot'].append(pivot)
            data['date'].append(date)
            data['time'].append(time)


        df = pd.DataFrame(data, index=data['symbol'])


        return df

    return None

if __name__ == '__main__':
    print('STARTING')
    print(next(20))
    print("************")
    print(next(40))