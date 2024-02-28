import os
import csv

Candidate_List = []
Total_Count_of_Votes = []
Stockham_Total = 0
DeGette_Total = 0
Doane_Total = 0

# Provide the entire file path using os.path.join()
election_csv_path = os.path.join("Resources", "election_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(election_csv_path, "r") as csvfile:
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

# Write results to a text file using f-string formatting
output_file = "PyPoll_analysis.txt"
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {len(Total_Count_of_Votes)}\n")
    file.write("-------------------------\n")
    file.write(f"Charles Casper Stockham: {Stockham_Percentage_of_Votes:.3f}% ({Stockham_Total})\n")
    file.write(f"Diana DeGette: {DeGette_Percentage_of_Votes:.3f}% ({DeGette_Total})\n")
    file.write(f"Raymon Anthony Doane: {Doane_Percentage_of_Votes:.3f}% ({Doane_Total})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner_name}\n")
    file.write("-------------------------\n")

print("Results have been saved to PyPoll_analysis.txt")