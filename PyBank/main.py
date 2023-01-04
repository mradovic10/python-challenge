# Import necessary modules.
import os
import csv

# Locate the CSV file to be read.
csvpath = os.path.join("Resources", "budget_data.csv")

# Create lists to hold information that will be pulled from the CSV file.
months = []
profit_losses = []
# Create a list to hold changes in profit/loss from month to month.
changes = []
# Create a variable for the purposes of figuring out monthly change. Its initial value is not important as our first result will be removed.
initial_pro_loss = 0

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

        # Get the profit/loss of the month that the loop is currently on.
        next_pro_loss = int(row[1])
        # Calculate the monthly change between the current month in the loop and the one preceeding it.
        monthly_change = next_pro_loss - initial_pro_loss

        # Store the monthly change in the "changes" list.
        changes.append(monthly_change)

        # Update the initial variable so the monthly change can be correctly calculated in the next loop.
        initial_pro_loss = next_pro_loss

# Remove the first value in the "changes" list becuase it does not mean anything and it skews the calculation of the average monthly change.
changes.pop(0)
# Calculate the average monthly change and round it to the second decimal point.
changes_avg = round(sum(changes) / len(changes), 2)
# Figure out the date that corresponds with the greatest positive monthly change. Since monthly change is calculated starting with the second date, 
# we move our index up by one.
max_date = months[(changes.index(max(changes))) + 1]
# Same thing as above, except it's figuring out the greatest negative monthly change.
min_date = months[(changes.index(min(changes))) + 1]

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
print(f"Average Change: ${changes_avg}")
print()
# Greatest positive monthly change over the entire period (date and amount).
print(f"Greatest Increase in Profits: {max_date} (${max(changes)})")
print()
# Greatest negative monthly change in profits over the entire period (date and amount).
print(f"Greatest Decrease in Profits: {min_date} (${min(changes)})")

# Create a path for a text file called "analysis."
analysispath = os.path.join("Analysis", "analysis.txt")

# Create a list of lines that are going to be written into the "analysis" text file ("" = empty line).
lines = ["Financial Analysis", "", "-----------------------------", "", 
        "Total Months: " + str(len(months)), "", 
        "Total: $" + str(sum(profit_losses)), "", 
        "Average Change: $" + str(changes_avg), "", 
        "Greatest Increase in Profits: " + str(max_date) + " ($" + str(max(changes)) + ")", "", 
        "Greatest Decrease in Profits: " + str(min_date) + " ($" + str(min(changes)) + ")"]

# Open "analysis.txt" to write into it.
with open(analysispath, 'w') as txtfile:

    # Loop throught the "lines" list.
    for line in lines:

        # Write the line.
        txtfile.write(line)

        # Move down to the next line in the text file.
        txtfile.write("\n")
