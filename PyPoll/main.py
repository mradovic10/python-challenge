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

def winner(lists):
    if charles_count > diana_count and raymon_count:
        print("Winner: Charles Casper Stockham")

    if diana_count > charles_count and raymon_count:
        print("Winner: Diana DeGette")

    if raymon_count > charles_count and diana_count:
        print("Winner: Raymon Anthony Doane")

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
winner([charles, diana, raymon])
print()
print("------------------------------")