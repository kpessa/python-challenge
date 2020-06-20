import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    votes_dictionary = {}
    votes_counter = 0 
    #Read each row of data after the header
    for row in csvreader:
        if row[2] in votes_dictionary:
            votes_dictionary[row[2]] += 1
        else:
            votes_dictionary[row[2]] = 1
        # accumulate votes_counter
        votes_counter += 1

    printStr = "Election Results\n"
    printStr += "-------------------------\n"
    printStr += f"Total Votes: {votes_counter}\n"
    printStr += "-------------------------\n"
    winner = [0,""]
    for key in votes_dictionary:
        percent_won = votes_dictionary[key]/votes_counter*100
        printStr += f"{key}: {percent_won:.3f}% ({votes_dictionary[key]})\n"
        if votes_dictionary[key] > winner[0]:
            winner = [votes_dictionary[key],key]
    printStr += "-------------------------\n"
    printStr += f"Winner: {winner[1]}\n"
    printStr += "-------------------------\n"

print(printStr)

outputfilepath = os.path.join("analysis",'analysis.txt')
with open(outputfilepath,'w') as f:
    f.write(printStr)