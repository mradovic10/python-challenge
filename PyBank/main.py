# Import necessary modules.
import os
import csv

# Locate the CSV file to be read.
csvpath = os.path.join("Resources", "budget_data.csv")

# Create lists to hold information that will be pulled from the CSV file.
months = []
profit_losses = []
changes = []

# Read file using CSV module and store it in "csvreader."
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the first row that contains the header.
    csvheader = next(csvfile)

    # Loop through each row in the CSV file.
    for row in csvreader:
        
        # Store the first column into the "months" list.
        months.append(row[0])

        # Store the second column into the "profit_losses" list.
        profit_losses.append(int(row[1]))

# Print out the required analysis to the terminal.
print()
print("Financial Analysis")
print()
print("-----------------------------")
print()
# Total number of months included in the data set.
print(f"Total Months: {len(months)}")
print()
# Net total amount of "Profit/Losses" over the entire period.
print(f"Total: ${sum(profit_losses)}")
print()
# Average amount of change over the entire period.
print(f"Average Change: $")
print()
# Greatest increase in profits over the entire period (date and amount).
print(f"Greatest Increase in Profits: ")
print()
# Greatest decrease in profits over the entire period (date and amount).
print(f"Greatest Decrease in Profits: ")

# Create a path for a text file called "analysis."
analysispath = os.path.join("Analysis", "analysis.txt")

# Create a list of lines that are going to be written into the "analysis" text file ("" = empty line).
lines = ["Financial Analysis", "", "-----------------------------", "", "Total Months: " + str(len(months)), "", "Total: $" + str(sum(profit_losses)), "", "Average Change: $", "", "Greatest Increase in Profits: ", "", "Greatest Decrease in Profits: "]

# Open "analysis.txt" to write into it.
with open(analysispath, 'w') as txtfile:

    # Loop throught the "lines" list.
    for line in lines:

        # Write the line.
        txtfile.write(line)

        # Move down to the next line in the text file.
        txtfile.write("\n")
