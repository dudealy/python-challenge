import os
import csv
csvpath=os.path.join('.', 'Resources', 'budget_data.csv')
month_length=0
total_profitLoss=0
average_profitLoss=float()

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    
 
    for row in csvreader:
        date=str(row[0])
        month_length+=1
        profitLoss=int(row[1])
        total_profitLoss+=profitLoss
        if row in profitLoss
        average_profitLoss=(total_profitLoss/month_length)



    print(date)    
    print("'''text")
    print("----------------------------")
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " +str(month_length))
    print("Total: " +str(total_profitLoss))
    print("Average Change: " +str(average_profitLoss))