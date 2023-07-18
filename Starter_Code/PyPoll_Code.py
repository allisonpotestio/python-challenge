import os
import csv

#connect csv
filepath=os.path.join("PyPoll","Resources","election_data.csv")

with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
#define columns??


#calculate total votes
votes_count=len('Votes')


#list % votes and count of votes for each candidate

#determine winner

#summary/output
print("Election Results")
print("-------------------------")
print(f'Total Votes: {votes_count}')
print("-------------------------")