import csv
import os


file_path = "./Resources/election_data.csv"
out_file="./Analysis/output.txt"


v_count = []
v_percent = []
cand_list = []
winner_cand = []
voter_id = []


with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        #The total number of months included in the dataset
        voter_id = voter_id + 1
        cand_list.append (row[2])
    for w set(cand_list):
        winner_cand.append(w)
        c = cand_list.count(c)
        t = (c/count)*100
        v_percent.append(1)

        



print(f"voter id: {voter_id}")

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

