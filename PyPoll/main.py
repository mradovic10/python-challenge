# Import necessary modules.
import os
import csv

# Locate the CSV file to be read.
csvpath = os.path.join("Resources", "election_data.csv")

charles = []
diana = []
raymon = []

# Read file using CSV module and store it in "csvreader."
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the first row that contains the header.
    csvheader = next(csvfile)

    for vote in csvreader:

        if vote[2] == "Charles Casper Stockham":
            charles.append(vote[2])

        if vote[2] == "Diana DeGette":
            diana.append(vote[2])

        if vote[2] == "Raymon Anthony Doane":
            raymon.append(vote[2])

total = len(charles) + len(diana) + len(raymon)

charles_percentage = round((len(charles) / total) * 100, 3)
charles_count = len(charles)

diana_percentage = round((len(diana) / total) * 100, 3)
diana_count = len(diana)

raymon_percentage = round((len(raymon) / total) * 100, 3)
raymon_count = len(raymon)

winner_list = []

def winner(lists):
    if charles_count > diana_count and raymon_count:
        winner_list.append("Winner: Charles Casper Stockham")

    if diana_count > charles_count and raymon_count:
        winner_list.append("Winner: Diana DeGette")

    if raymon_count > charles_count and diana_count:
        winner_list.append("Winner: Raymon Anthony Doane")

winner([charles, diana, raymon])

print()
print("Election Results")
print()
print("------------------------------")
print()
print(f"Total Votes: {total}")
print()
print("------------------------------")
print()
print(f"Charles Casper Stockham: {charles_percentage}% ({charles_count})")
print()
print(f"Diana DeGette: {diana_percentage}% ({diana_count})")
print()
print(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_count})")
print()
print("------------------------------")
print()
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
