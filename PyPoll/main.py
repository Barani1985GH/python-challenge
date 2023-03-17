# Modules
import os
import csv

# Declare a variables 
election_data = []  # To store all elecyion data records inside a list
candidates = ["Charles Casper Stockham","Raymon Anthony Doane","Diana DeGette"]

# initialize vote count of all 3 candidates
Charles_vote_count = 0
Raymon_vote_count = 0
Diana_vote_count = 0

# Dict to store vote summary
vote_summary = {}


# Set path to csv file
csvpath = os.path.join("Resources", "election_data.csv")
analysispath = os.path.join("Analysis","analysis.txt")

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    
    # calculate total number of votes cast
    for row in csvreader:
        election_data.append(row) 
    
    # calculate each candidates vote and their vote percent 
    for row in election_data:
        if (row["Candidate"] == candidates[0]):
            Charles_vote_count = Charles_vote_count + 1
        if (row["Candidate"] == candidates[1]):
            Raymon_vote_count = Raymon_vote_count + 1
        if (row["Candidate"] == candidates[2]):
            Diana_vote_count = Diana_vote_count + 1
    
    vote_summary = {candidates[0]:Charles_vote_count,candidates[2]:Diana_vote_count,candidates[1]:Raymon_vote_count}
    
print("\nElection Results\n\n----------------------------")

# The total number of votes cast
print ("\nTotal Votes: ",len(election_data) )

print("\n----------------------------\n\n")

# A complete list of candidates who received votes,The percentage of votes each candidate won,The total number of votes each candidate
print (candidates[0],":",round(((Charles_vote_count/len(election_data))*100),3),"%  (",Charles_vote_count,")\n" )
print (candidates[2],":",round(((Diana_vote_count/len(election_data))*100),3),"%  (",Diana_vote_count,")\n" )
print (candidates[1],":",round(((Raymon_vote_count/len(election_data))*100),3),"%  (",Raymon_vote_count,")\n" )

print("\n----------------------------\n")

#The winner of the election based on popular vote
winner = max(vote_summary, key=vote_summary.get)
print("Winner: ",winner)

print("\n----------------------------\n")

analysis = ["\nElection Results\n\n----------------------------","\nTotal Votes: ",len(election_data),"\n----------------------------\n\n",candidates[0],":",round(((Charles_vote_count/len(election_data))*100),3),"%  (",Charles_vote_count,")\n",candidates[2],":",round(((Diana_vote_count/len(election_data))*100),3),"%  (",Diana_vote_count,")\n",candidates[1],":",round(((Raymon_vote_count/len(election_data))*100),3),"%  (",Raymon_vote_count,")\n","\n----------------------------\n","Winner: ",winner,"\n----------------------------\n"]
with open(analysispath,'w') as file:
    for i in analysis:
     file.write(str(i))



