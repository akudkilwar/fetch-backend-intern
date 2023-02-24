from collections import OrderedDict
import csv
import datetime
import sys


# returns a list in sorted order by date by parsing csv.
def extractSortedListFromCSV(csv_name="transactions.csv"):
    date_format = "%Y-%m-%dT%H:%M:%SZ"

    with open(csv_name, 'r') as file:
        # Return a reader object which will iterate over lines in the given csvfile
        csv_reader = csv.reader(file)
    
        # convert string to list
        csv_rows = list(csv_reader)[1:] # omit labels

        for row in csv_rows:
            timestamp = row[2]
            date = datetime.datetime.strptime(timestamp, date_format)       
            row.append(date)
        
        csv_rows.sort(key=lambda x:x[3]) # sort according to oldest datetime earliest

    return csv_rows



# returns the dictionary with payer balances such that oldest transactions are first and no negative balances.
def getPayerPointBalances(csv_rows, balance=5000):
    ht = OrderedDict() # use OrderedDict instead of regular Dict to preserve transaction order by date.
    flag = 0

    for [payer, points, timestamp, date] in csv_rows:
        # make sure every payer has an entry/default value in the hash table
        if payer not in ht:
            ht[payer] = 0

        points = int(points) # casting points in csv from string to int
        if points <= balance and flag == 0:
            balance -= points
        else:
            if flag == 0:
                flag = 1 # once the flag is switched, a section of the code (line 40-46) will be unreachable
                ht[payer] = points - balance
            else:
                ht[payer] += points

    # handling negative payer balances
    payers_to_settle = [] 
    for payer in ht:
        if ht[payer] < 0:
            payers_to_settle.append(payer)
    
    for payer in payers_to_settle:
        points_to_distribute = abs(ht[payer])
        for key in ht:
            if key == payer:
                continue
            if ht[key] > 0: # not enough balance to distribute all points
                # print(ht[key], key, points_to_distribute)
                if ht[key] < points_to_distribute:
                    points_to_distribute -= ht[key]
                    ht[key] = 0
                else: # enough balance to distribute points
                    ht[key] -= points_to_distribute
                    points_to_distribute = 0 # formality
                    ht[payer] = points_to_distribute # all points have been distributed
                    break
    return dict(ht)
    


def main():
    if len(sys.argv) != 3 or sys.argv[2][-4:] != ".csv":
        print("Usage: python3 mycode.py <points to spend> <csv file name>")
        return

    print(getPayerPointBalances(extractSortedListFromCSV(sys.argv[2]), balance=int(sys.argv[1])))


if __name__ == '__main__':
    main()