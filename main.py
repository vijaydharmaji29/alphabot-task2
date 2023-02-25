import brain
import data_giver as dg
import executioner
import csv

capital = 10000000
positions = []

i = 0

all_actions = []

while True:
    try:
        print("INDEXING - ", i)
        n = dg.next(i)

        execute = brain.calculate(capital, n, positions)
        capital, executed, positions = executioner.trade(execute, capital, positions)

        for j in executed:
            all_actions.append(j)
    except:
        break

    i+=1

eval = capital
for i in positions:
    eval += i.buy_val

print(eval)

# writing to csv file
with open('actions.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the data rows
    csvwriter.writerows(all_actions)

# if __name__ == '__main__':
#     n = dg.next(10)
#
#     execute = brain.calculate(1000000, n)
#
#     print(execute)