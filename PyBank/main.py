import csv
import os

init_profit = 0
total_profit = 0
count = 0
total_change = []

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
        date = []
        profit = []
       #The net total amount of "Profit/Losses" over the entire period
       
        



#print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")


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
