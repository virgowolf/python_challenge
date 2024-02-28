import os
import csv

# Provide the file path using os.path.join()
budget_csv_path = os.path.join("Resources", "budget_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Initialize variables
total_months = 0
net_total = 0
changes = []
previous_profit_loss = 0
greatest_increase_amount = 0
greatest_decrease_amount = 0
greatest_increase_date = ""
greatest_decrease_date = ""
# Create a boolean variable to flag first month since Jan has nothing to compare to
is_first_month = True

with open(budget_csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csv_reader)

    # Start the loop from row 4 onwards
    for row in csv_reader:
        # Calculate total months
        total_months += 1

        # Calculate net total
        profit_loss = int(row[1])
        net_total += profit_loss

        # Calculate changes and update greatest increase and decrease
        if is_first_month:
            is_first_month = False
            
        else:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            if change > greatest_increase_amount:
                greatest_increase_amount = change
                greatest_increase_date = row[0]

            if change < greatest_decrease_amount:
                greatest_decrease_amount = change
                greatest_decrease_date = row[0]

        previous_profit_loss = profit_loss

# Calculate average change
print(changes)
total_changes = len(changes)
average_change = sum(changes) / total_changes

# Display results in the console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

# Write results to a text file using f-string formatting
output_file = "PyBank_budget_analysis.txt"
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

print("Results have been saved to PyBank_budget_analysis.txt")
