import os
import csv

pollData = os.path.join("Starter_Code","PyPoll/Resources","election_data.csv")


with open(pollData, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # total votes
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

  # candidate count -- who received votes
    candidatelist = list()
    total_candidate = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        total_candidate.append(candidate)
        if candidate not in candidatelist: 
            candidatelist.append(candidate)
    candicount = len(candidatelist)

  # Total Number of Votes for each candidate
    votes = list()
    percentage = list()
    for j in range (0,candicount):
        name = candidatelist[j]
        votes.append(total_candidate.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

    winner = votes.index(max(votes))    


    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,candicount): 
        print(f"{candidatelist[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidatelist[winner]}")
    print("----------------------------")

  # Print the results to "PyPoll.txt" file
    print("Election Results", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    for k in range (0,candicount): 
        print(f"{candidatelist[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Winner: {candidatelist[winner]}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
