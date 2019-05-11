import os
import csv
csvpath=os.path.join('.', 'Resources', 'budget_data.csv')
month_length=0
total_profitLoss=0
average_profitLoss=float()
average_diff=[]
starter_diff=867884
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    
    count = 0
    val = None

    for row in csvreader:
        if count == 0:
            val = row
        else:
            #append diff to average_diff []
            # int(row[1]) - int(val[1])
            print('current_row: {}, previous_row: {}'.format(row[1], val[1]))
            val = row

        count +=1
    
#         date=str(row[0])
#         month_length+=1
#         profitLoss=int(row[1])
#         total_profitLoss+=profitLoss
#         for val in profitLoss:
#             average_diff.append(starter_diff-val)
#             print(average_diff)
#     # average_profitLoss=(total_profitLoss/month_length)

#     print(date)    
#     print("'''text")
#     print("----------------------------")
#     print("Financial Analysis")
#     print("----------------------------")
#     print("Total Months: " +str(month_length))
#     print("Total: " +str(total_profitLoss))
#     print("Average Change: " +str(average_profitLoss))



#      # if row in profitLoss
    

#         # for ave_rage in profitLoss:
#         #     if rage_starter>ave_rage:
#         #         rage

# # average_list[]
# # rage_starter =0