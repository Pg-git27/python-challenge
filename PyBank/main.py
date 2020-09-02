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
greatest_inc_amount = 0
greatest_inc_datemonth = ""
greatest_dec_amount = 0
greatest_dec_datemonth = ""


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    
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
            #print (month_change)
            diff_ProfitLoss = int(row[1]) - prev_profit_loss
            #print("Difference in P-L" + str(diff_ProfitLoss))
            #To calculate avg.
        total_changeinPL += diff_ProfitLoss   
        
        prev_profit_loss = int(row[1])
        #print("previous profitloss" + str(prev_profit_loss))
        
        
        # The greatest increase in profits (date and amount) over the entire period
        if diff_ProfitLoss > greatest_inc_amount:
            greatest_inc_amount = diff_ProfitLoss
            greatest_inc_datemonth = row[0]
        
        # The greatest decrease in losses (date and amount) over the entire period
        if diff_ProfitLoss < greatest_dec_amount:
            greatest_dec_amount = diff_ProfitLoss
            greatest_dec_datemonth = row[0]

# The average of the changes in "Profit/Losses" over the entire period.        
avg_ProfitLoss = total_changeinPL / (total_months - 1)

# Print the analysis to terminal
print("Financial Analysis")
print("----------------------------")        
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(format(avg_ProfitLoss, '.2f')))
print("Greatest Increase in Profits: " + greatest_inc_datemonth + " ($" + str(greatest_inc_amount) + ")")
print("Greatest Decrease in Profits: " + greatest_dec_datemonth + " ($" + str(greatest_dec_amount) + ")")

# Write to text file Analysis_PyBank.txt
f = open("Analysis_PyBank.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")        
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total: $" + str(total_profit_loss) + "\n")
f.write("Average Change: $" + str(format(avg_ProfitLoss, '.2f')) + "\n")
f.write("Greatest Increase in Profits: " + greatest_inc_datemonth + " ($" + str(greatest_inc_amount) + ")\n")
f.write("Greatest Decrease in Profits: " + greatest_dec_datemonth + " ($" + str(greatest_dec_amount) + ")\n")
f.close()