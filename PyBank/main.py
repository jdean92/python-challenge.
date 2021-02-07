import csv
import os

init_profit = 0
total_profit = 0
total_months = 0
total_change = []
profit = []
date = []


file_path = "./Resources/budget_data.csv"
out_file="./Analysis/output.txt"

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
   
    # Read each row of data after the header

    for row in csvreader:
        #The total number of months included in the dataset
        total_months = total_months + 1
        date.append (row[0])
        profit.append (int(row[1]))
    
    for v in profit:
        total_profit = total_profit + v

    for c in range(1, len(profit)):
        total_change.append(int(profit[c]) - int(profit[c-1]))

increase_profit = max(total_change)
decrease_profit = min(total_change)
maxum_date = date[total_change.index(increase_profit) + 1]
decrease_date = date[total_change.index(decrease_profit) + 1]
avgerage_change = sum(total_change) / len(total_change)





#print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"increased profits {maxum_date} {increase_profit}")
print(f"decreased profits {decrease_date} {decrease_profit}")
print(f"avgerage change:{round(avgerage_change,2)}")
print(f"total profit:{total_profit}")


#write to file
with open(out_file,'w') as outputFile:
    outputFile.write("Financial Analysis")
    outputFile.write("Financial Analysis")
    outputFile.write("----------------------------")
    outputFile.write(f"Total Months: {total_months}")

# results should look like
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
