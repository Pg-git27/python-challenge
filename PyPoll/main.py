#PYPOLL-Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Set variables
total_numvotes = 0
candidate = ""
candidate_list = []
vote_list = []
percent_list = []
winner = ""

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
   
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # count the total number of votes
        total_numvotes += 1
        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidate_list.index(row[2])] += 1

# Calculate the percentage of vote            
percent_list = [(100/total_numvotes) * x for x in vote_list]

# Find the winner
winner = candidate_list[vote_list.index(max(vote_list))]

# Print the analysis to terminal       
print("Election Results")
print("-------------------------")
print("The total number of votes cast: " + str(total_numvotes))
print("-------------------------")
print("The percentage of votes each candidate won: ")
for x in candidate_list:
    print(x + ": " + str(format(percent_list[candidate_list.index(x)], '.3f')) 
        + "% (" + str(vote_list[candidate_list.index(x)]) + ")")
    
print("-------------------------")
print("The winner of the election based on popular vote: " + winner)
print("-------------------------")

# Write to text file Analysis_PyPoll
f = open("Analysis_PyPoll.txt", "w")

f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(total_numvotes) + "\n")
f.write("-------------------------\n")

for x in candidate_list:
    f.write(x + ": " + str(format(percent_list[candidate_list.index(x)], '.3f')) 
        + "% (" + str(vote_list[candidate_list.index(x)]) + ")\n")
    
f.write("-------------------------\n")
f.write("Winner: " + winner + "\n")
f.write("-------------------------\n")

f.close()