#PYBANK-Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set variables
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
diff_ProfitLoss = 0
total_changeinPL = 0
avg_ProfitLoss = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_increase_month = ""

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
#The total number of months included in the dataset
        total_months += 1
        
#The net total amount of "Profit/Losses" over the entire period
        total_profit_loss += int(row[1])
        
        # calculate the change in profit/loss
        if total_months > 1:
            #month_change = int(row[1]) - prev_profit_loss
            diff_ProfitLoss = int(row[1]) - prev_profit_loss
            #print("Difference in P-L" + str(diff_ProfitLoss))
        total_changeinPL += diff_ProfitLoss   # This is used to calculate avg
        
        prev_profit_loss = int(row[1])
        #print("previous profitloss" + str(prev_profit_loss))
        
        
        # The greatest increase in profits (date and amount) over the entire period
        if diff_ProfitLoss > greatest_increase:
            greatest_increase = diff_ProfitLoss
            greatest_increase_month = row[0]
        
        # The greatest decrease in losses (date and amount) over the entire period
        if diff_ProfitLoss < greatest_decrease:
            greatest_decrease = diff_ProfitLoss
            greatest_decrease_month = row[0]

# The average of the changes in "Profit/Losses" over the entire period.        
avg_ProfitLoss = total_changeinPL / (total_months - 1)

# Print the analysis to terminal
print("Financial Analysis")
print("----------------------------")        
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(format(avg_ProfitLoss, '.2f')))
print("Greatest Increase in Profits: " + greatest_increase_month 
      + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month 
      + " ($" + str(greatest_decrease) + ")")

# Write to text file Analysis_PyBank.txt
f = open("Analysis_PyBank.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")        
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total: $" + str(total_profit_loss) + "\n")
f.write("Average Change: $" + str(format(avg_ProfitLoss, '.2f')) + "\n")
f.write("Greatest Increase in Profits: " + greatest_increase_month 
      + " ($" + str(greatest_increase) + ")\n")
f.write("Greatest Decrease in Profits: " + greatest_decrease_month 
      + " ($" + str(greatest_decrease) + ")\n")
f.close()