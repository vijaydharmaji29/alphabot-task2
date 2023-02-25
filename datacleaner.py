import os
import csv

tickers = os.listdir('big_data/')
l = []

for i in tickers:
    with open('big_data/' + i) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                date = row[1]
                if '2017-07-03' not in date:
                    l.append(i)

                break
print(l)
for i in l:
    os.remove('big_data/' + i)