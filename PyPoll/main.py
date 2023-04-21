import os
import csv

pypoll_path = os.path.join('Resources','election_data.csv')
createfilepath = os.path.join('analysis', 'PyPollanalysis.txt')

TotalVotes = 0
Percnt = 0
Cand = []
Cdict = {}

with open(pypoll_path, 'r') as pypolldata:
    
    csvreader = csv.reader(pypolldata,delimiter=",")
    header = next(csvreader)
    for row in csvreader:

        TotalVotes += 1
        
        if row[2] not in Cand:
            Cand.append(row[2])
            Cdict[row[2]] = 1
            
        else:
            Cdict[row[2]] += 1

    
Can1 = Cdict["Charles Casper Stockham"]
Can1VotesPer = round((Can1 / TotalVotes), 5)
Can1VotesPerc = format((Can1VotesPer), '.3%')
Cdict['Charles Casper Stockham'] = [Can1VotesPerc, Cdict['Charles Casper Stockham']]

Can2 = Cdict["Diana DeGette"]
Can2VotesPer = round((Can2 / TotalVotes), 5)
Can2VotesPerc = format((Can2VotesPer), '.3%')
Cdict['Diana DeGette'] = [Can2VotesPerc, Cdict['Diana DeGette']]

Can3 = Cdict["Raymon Anthony Doane"]
Can3VotesPer = round((Can3 / TotalVotes), 5)
Can3VotesPerc = format((Can3VotesPer), '.3%')
Cdict['Raymon Anthony Doane'] = [Can3VotesPerc, Cdict['Raymon Anthony Doane']]

print(" " + "\n")
print("Election Results"+ "\n")
print("-------------------------"+ "\n")
print("Total Votes: " + str(TotalVotes)+ "\n")
print("-------------------------"+ "\n")
print("Charles Casper Stockham: " + Cdict["Charles Casper Stockham"][0] + " (" + str(Cdict["Charles Casper Stockham"][1]) + ")"+ "\n") 
print("Diana DeGette: " + Cdict["Diana DeGette"][0] + " (" + str(Cdict["Diana DeGette"][1]) + ")"+ "\n")
print("Raymon Anthony Doane: " + Cdict["Raymon Anthony Doane"][0] + " (" + str(Cdict["Raymon Anthony Doane"][1]) + ")"+ "\n")
print("-------------------------"+ "\n")
print("Winner: Diana DeGette"  + "\n")
print("-------------------------")

with open(createfilepath, 'w') as f:
    f.write(" " + "\n")
    f.write("Election Results" + "\n")
    f.write(" " + "\n")
    f.write("-------------------------" + "\n")
    f.write(" " + "\n")
    f.write("Total Votes: " + str(TotalVotes) + "\n")
    f.write(" " + "\n")
    f.write("-------------------------" + "\n")
    f.write(" " + "\n")
    f.write("Charles Casper Stockham: " + Cdict["Charles Casper Stockham"][0] + " (" + str(Cdict["Charles Casper Stockham"][1]) + ")" + "\n") 
    f.write(" " + "\n")
    f.write("Diana DeGette: " + Cdict["Diana DeGette"][0] + " (" + str(Cdict["Diana DeGette"][1]) + ")" + "\n")
    f.write(" " + "\n")
    f.write("Raymon Anthony Doane: " + Cdict["Raymon Anthony Doane"][0] + " (" + str(Cdict["Raymon Anthony Doane"][1]) + ")" + "\n")
    f.write(" " + "\n")
    f.write("-------------------------" + "\n")
    f.write(" " + "\n")
    f.write("Winner: Diana DeGette" + "\n")
    f.write(" " + "\n")
    f.write("-------------------------" + "\n")