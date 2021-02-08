import csv
import os


file_path = "./Resources/election_data.csv"
out_file="./Analysis/output.txt"

voter_id = []
voter_can = []
county = []

v_count = 0
count = 0
v_percent = 0
cand_list = {"Candidate": [], "Votes": [], "Vote Perc": []}
winner_cand = 0


with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:

        count = count +1
    for u in cand_list["Candidate"]:
        index = cand_list["Candidate"].index(u)
        file_path.write(f"{u}: {cand_list['Vote Perc'][indx]}% ({cand_list['Votes'][indx]})\n")

        #The total number of months included in the dataset
        #voter_id = voter_id + 1
        
        #cand_list.append (row[2])

    # for w in cand_list:

        #if any ([True for k,v in cand_list.items() ]):
        # if w in cand_list:
        #     v_count = cand_list[w[2]]
        #     cand_list[w[2]] = v_count +1

        # else:  
        #     cand_list[w[2]] = 1


            
        # if voter_can > winner_cand:
        #     winner_cand = v_count

        #     winner_cand.append(w)
        #     c = cand_list.count(w)
        #     v_count.append(c)
        #     d = (c/count)*100
for i in len(cand_list):
    print (f"{cand_list[i]}: {v_percent}% ")



# print(f"Total Votes: {count}")
# print(f"increased profits {maxum_date} {increase_profit}")
# print(f"decreased profits {decrease_date} {decrease_profit}")
# print(f"avgerage change:{round(avgerage_change,2)}")
# print(f"total profit:{total_profit}")

print("Election Results")

print("--------------------------")

#print(f" Total Votes: {}") 

print("--------------------------")

#for name, v_count in v_count.items():
    
#print(f"{winner_cand}: {v_percent[winner_cand]} ({v_count})")
    
#print("--------------------------")

#print(f"AND the Winner is: {v_count}!")

#print("--------------------------")




#print(f"v_count: {v_count}")

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

