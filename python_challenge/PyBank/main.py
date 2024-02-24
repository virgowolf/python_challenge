import os
import csv

# Provide the entire file path using os.path.join()
budget_csv = os.path.join("/Users/celinakamler/Desktop/UCB Data Viz Class Folder/Challenge 3/python_challenge/PyBank", "budget_data.csv")

with open(budget_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# Initialize variables
    total_months = 0
    net_total = 0
    changes = []
    previous_profit_loss = 0
    greatest_increase_amount = 0
    greatest_decrease_amount = 0
    greatest_increase_date = ""
    greatest_decrease_date = ""

    # Skip the header row
    next(csv_reader, None)

    for row in csv_reader:
        # Calculate total months
        total_months += 1

        # Calculate net total
        profit_loss = int(row[1])
        net_total += profit_loss

        # Calculate changes and average change
        change = profit_loss - previous_profit_loss
        changes.append(change)
        previous_profit_loss = profit_loss

        # Find greatest increase in profits
        if change > greatest_increase_amount:
            greatest_increase_amount = change
            greatest_increase_date = row[0]

        # Find greatest decrease in profits
        if change < greatest_decrease_amount:
            greatest_decrease_amount = change
            greatest_decrease_date = row[0]

    # Calculate average change
    average_change = sum(changes) / len(changes)

    # Output file
    output_file = os.path.join(os.getcwd(), "PyBank_budget_analysis.csv")

    with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)

        # Write the header row
        writer.writerow(["Total Months", "Total Profit/Loss", "Average Change", "Greatest Increase Date", "Greatest Increase Amount", "Greatest Decrease Date", "Greatest Decrease Amount"])

        # Write the data
        writer.writerow([total_months, net_total, average_change, greatest_increase_date, greatest_increase_amount, greatest_decrease_date, greatest_decrease_amount])
