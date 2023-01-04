# Import necessary modules.
import os
import csv

# Locate the CSV file to be read.
csvpath = os.path.join("Resources", "election_data.csv")

# Create lists to hold votes for each individual candidate.
charles = []
diana = []
raymon = []

# Read file using CSV module and store it in "csvreader."
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the first row that contains the header.
    csvheader = next(csvfile)

    # Loop through each row in the CSV file.
    for vote in csvreader:

        # When there is a vote for Charles, add it to the "charles" list.
        if vote[2] == "Charles Casper Stockham":
            charles.append(vote[2])
        
        # When there is a vote for Diana, add it to the "diana" list.
        if vote[2] == "Diana DeGette":
            diana.append(vote[2])

        # When there is a vote for Raymon, add it to the "raymon" list.
        if vote[2] == "Raymon Anthony Doane":
            raymon.append(vote[2])

# Add up the lenghts of all three lists to get the total vote count.
total = len(charles) + len(diana) + len(raymon)

# Calculate the vote percentage for Charles and round the value to the third decimal point.
charles_percentage = round((len(charles) / total) * 100, 3)
# Calculate the number of votes for Charles.
charles_count = len(charles)

# Calculate the vote percentage for Diana and round the value to the third decimal point.
diana_percentage = round((len(diana) / total) * 100, 3)
# Calculate the number of votes for Diana.
diana_count = len(diana)

# Calculate the vote percentage for Raymon and round the value to the third decimal point.
raymon_percentage = round((len(raymon) / total) * 100, 3)
# Calculate the number of votes for Raymon.
raymon_count = len(raymon)

# Create a list that will hold the line to be written as to who the winner of the election is.
winner_list = []

# Create a function that will take the three candidate lists and figure out which one has the most votes.
def winner(lists):
    # If Charles has the most votes, then add his winner line to the "winner_list."
    if charles_count > diana_count and raymon_count:
        winner_list.append("Winner: Charles Casper Stockham")

    # If Diana has the most votes, then add her winner line to the "winner_list."
    if diana_count > charles_count and raymon_count:
        winner_list.append("Winner: Diana DeGette")

    # If Raymon has the most votes, then add his winner line to the "winner_list."
    if raymon_count > charles_count and diana_count:
        winner_list.append("Winner: Raymon Anthony Doane")

# Activate the above function.
winner([charles, diana, raymon])

# Print out the required analysis to the terminal.
print()
print("Election Results")
print()
print("------------------------------")
print()
# Total number of votes in all.
print(f"Total Votes: {total}")
print()
print("------------------------------")
print()
# Percent and count of the vote for Charles.
print(f"Charles Casper Stockham: {charles_percentage}% ({charles_count})")
print()
# Percent and count of the vote for Diana.
print(f"Diana DeGette: {diana_percentage}% ({diana_count})")
print()
# Percent and count of the vote for Raymon.
print(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_count})")
print()
print("------------------------------")
print()
# Print out the first and only line of the "winner_list" to announce the winner.
print(winner_list[0])
print()
print("------------------------------")

# Create a path for a text file called "analysis."
analysispath = os.path.join("Analysis", "analysis.txt")

# Create a list of lines that are going to be written into the "analysis" text file ("" = empty line).
lines = ["Election Results", "", "------------------------------", "", "Total Votes: " + str(total), "", "------------------------------", "", 
        "Charles Casper Stockham: " + str(charles_percentage) + "% (" + str(charles_count) + ")", "", 
        "Diana DeGette: " + str(diana_percentage) + "% (" + str(diana_count) + ")", "", 
        "Raymon Anthony Doane: " + str(raymon_percentage) + "% (" + str(raymon_count) + ")", "", 
        "------------------------------", "", winner_list[0], "", "------------------------------"]

# Open "analysis.txt" to write into it.
with open(analysispath, 'w') as txtfile:

    # Loop throught the "lines" list.
    for line in lines:

        # Write the line.
        txtfile.write(line)

        # Move down to the next line in the text file.
        txtfile.write("\n")
