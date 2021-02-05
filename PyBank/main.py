
total_months = 0

total_profit_loss_amount = 0.00

average_profit_loss = 0.00
greatest_increase = {}

greatest_decrease = {}


import csv
file_path = "./Resources/budget_data.csv"

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header

    for row in csvreader:
        #The total number of months included in the dataset
        total_months = total_months + 1
       #The net total amount of "Profit/Losses" over the entire period
        #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        #The greatest increase in profits (date and amount) over the entire period
        #The greatest decrease in losses (date and amount) over the entire period




#print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")



# results should look like
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
