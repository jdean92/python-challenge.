import csv
import os


file_path = "./Resources/election_data.csv"
out_file="./Analysis/output.txt"


v_count = []
v_percent = []
cand_list = []
diffrent_cand = []
count = []


with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        #The total number of months included in the dataset
        cand_list = cand_list + 1
        diffrent_cand.append (row[0])
        v_count.append (int(row[1]))



print(f"vote count: {v_count}")

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

