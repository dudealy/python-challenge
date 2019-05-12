import os
import csv
csvpath=os.path.join('.', 'Resources', 'budget_data.csv')
total_profitLoss=0
average_diff=[]
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    
    count = 0
    val = None

    for row in csvreader:
        if count == 0:
            val = row
        else:
         
            diff=int(row[1]) - int(val[1])
            average_diff.append(diff)
            val = row
        count +=1
        total_profitLoss= total_profitLoss=+int(row[1])
    average_of_proloss=(sum(average_diff)/(count-1))
     

    print("")
    print("----------------------------")
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " +(str(count)))
    print("Total: " +str(total_profitLoss))
    print("Average Change: " + "{:.{}f}".format(average_of_proloss, 2))
    print("Greatest Change: " + str(max(average_diff)))
    print("Lowest Change: " + str(min(average_diff)))