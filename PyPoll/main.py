import csv
import os


file_path = "./Resources/election_data.csv"
out_file="./Analysis/output.txt"

voter_id = []
voter_can = []
county = []

v_count = 0
results = []
v_percent = 0
cand_list = {}
winner_cand = 0
vote_won = 0

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        #The total number of months included in the dataset
        #voter_id = voter_id + 1
        v_count +=1
        cand_list.append (row[2])

    for w in set(cand_list):
        #if any ([True for k,v in cand_list.items() ]):
        #if w in cand_list:
        results.append(w)
        v_count.append(cand_list.count(w))
        v_percent.append((cand_list.count(w)/v_count)*100)
        cand_list +=1


        #else:  

        if voter_can > winner_cand:
            winner_cand = v_count




#print(f"vote won: {vote_won}")

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

