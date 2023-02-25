import os

import pandas as pd
import data_collection as dc

# tickers = os.listdir('big_data/')
tickers = ['NIFTYBANK']

print('GETTING STOCK DATA')

stocks_data = {}

#getting data for all stocks in the timeframe
for t in tickers:
    ticker_data = dc.get_data()
    stocks_data[t] = ticker_data

def next(index):

    if index < len(stocks_data[tickers[0]]):
        data = {
            'symbol': [], 'close':[], 'filt': [], 'close_dif': [], 'direction':[], 'pivot': [],'date': []
        }

        for t in tickers:
            symbol = stocks_data[t].iloc[index].symbol
            close = stocks_data[t].iloc[index]['close']
            filt = stocks_data[t].iloc[index]['filt']
            close_dif = stocks_data[t].iloc[index]['close_dif']
            direction = stocks_data[t].iloc[index]['direction']
            pivot = stocks_data[t].iloc[index]['pivot']
            date = stocks_data[t].iloc[index]['datetime']

            data['symbol'].append(symbol)
            data['close'].append(close)
            data['filt'].append(filt)
            data['close_dif'].append(close_dif)
            data['direction'].append(direction)
            data['pivot'].append(pivot)
            data['date'].append(date)


        df = pd.DataFrame(data, index=data['symbol'])

        return df

    return None

if __name__ == '__main__':
    print('STARTING')
    print(next(20))
    print("************")
    print(next(40))