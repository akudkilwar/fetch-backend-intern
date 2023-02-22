import csv
import datetime
# modular code, try to keep things flexible/modifiable. Abstain from hardcoding.

def extractSortedListFromCSV(csv_name="transactions.csv"):
    date_format = "%Y-%m-%dT%H:%M:%SZ"

    with open(csv_name, 'r') as read_obj:
        # Return a reader object which will iterate over lines in the given csvfile
        csv_reader = csv.reader(read_obj)
    
        # convert string to list
        csv_rows = list(csv_reader)[1:] # omit labels
        print(csv_rows)


        for row in csv_rows:
            timestamp = row[2]
            date = datetime.datetime.strptime(timestamp, date_format)       
            print(date)
            row.append(date)
        
        csv_rows.sort(key=lambda x:x[3]) # sort according to oldest datetime earliest

        for row in csv_rows:
            print(row)
        
    return csv_rows

def getPayerPointBalances(csv_rows, balance=5000):
    ht = {}
    flag = 0

    for [payer, points, timestamp, date] in csv_rows:
        if payer not in ht:
            ht[payer] = 0

        points = int(points)
        if points <= balance and flag == 0:
            balance -= points
        else:
            if flag == 0:
                flag = 1
                ht[payer] = points - balance
            else:
                ht[payer] += points
    
    print(ht)
    return ht
    



getPayerPointBalances(extractSortedListFromCSV())

        