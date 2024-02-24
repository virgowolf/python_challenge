import os
import csv

Candidate_List = []
Total_Count_of_Votes = []
Stockham_Total = 0
DeGette_Total = 0
Doane_Total = 0

election_csv = os.path.join("/Users/celinakamler/Desktop/UCB Data Viz Class Folder/Challenge 3/python_challenge/PyPoll", "election_data.csv")

with open(election_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Separate out the header row
    header = next (csvfile)
    print ("Header"+ header)

    for row in csv_reader:
        Total_Count_of_Votes.append(int(row[0])) #convert to integer
        Candidate_List.append(row[2])

        if row[2] == "Charles Casper Stockham":
            Stockham_Total += 1
        elif row[2] == "Diana DeGette":
            DeGette_Total += 1
        elif row[2] == "Raymon Anthony Doane":
            Doane_Total += 1

Stockham_Percentage_of_Votes = (Stockham_Total / len(Total_Count_of_Votes) * 100)
DeGette_Percentage_of_Votes = (DeGette_Total / len(Total_Count_of_Votes) * 100)
Doane_Percentage_of_Votes = (Doane_Total / len(Total_Count_of_Votes) * 100)

winner = max(Stockham_Percentage_of_Votes, DeGette_Percentage_of_Votes, Doane_Percentage_of_Votes)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(Total_Count_of_Votes)}")
print("-------------------------")
print(f"Charles Casper Stockham: {Stockham_Percentage_of_Votes:.3f}% ({Stockham_Total})")
print(f"Diana DeGette: {DeGette_Percentage_of_Votes:.3f}% ({DeGette_Total})")
print(f"Raymon Anthony Doane: {Doane_Percentage_of_Votes:.3f}% ({Doane_Total})")
print("-------------------------")

# Calculate the winner based on the popular vote
winner_name = ""
winner_votes = 0
for i in range(len(Candidate_List)):
    if Candidate_List[i] == "Charles Casper Stockham" and Total_Count_of_Votes[i] > winner_votes:
        winner_name = "Charles Casper Stockham"
        winner_votes = Total_Count_of_Votes[i]
    elif Candidate_List[i] == "Diana DeGette" and Total_Count_of_Votes[i] > winner_votes:
        winner_name = "Diana DeGette"
        winner_votes = Total_Count_of_Votes[i]
    elif Candidate_List[i] == "Raymon Anthony Doane" and Total_Count_of_Votes[i] > winner_votes:
        winner_name = "Raymon Anthony Doane"
        winner_votes = Total_Count_of_Votes[i]

# Print the winner based on the popular vote
print(f"Winner: {winner_name}")
print("-------------------------")