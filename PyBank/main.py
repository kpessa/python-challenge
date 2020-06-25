import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #Read each row of data after the header
    netTotal = 0
    numMonths = 0
    greatestIncrease = ["",0]
    greatestDecrease = ["",0]
    change_in_profits = 0
    previousProfitLoss = 0

    for row in csvreader:
        currentProfitLoss = int(row[1])
        if iter(csvreader).line_num != 2:
            change_in_profits += currentProfitLoss - previousProfitLoss
        if currentProfitLoss > int(greatestIncrease[1]):
            greatestIncrease = row
        if currentProfitLoss < int(greatestDecrease[1]):
            greatestDecrease = row 

        netTotal += currentProfitLoss
        numMonths += 1
        previousProfitLoss = currentProfitLoss
    
    

    printStr = f"\nTotal Months: {numMonths}\n"    
    printStr += f"Total: ${netTotal:,}\n"
    printStr += f"Average Change: ${round(change_in_profits/(numMonths-1),2):,}\n"
    printStr += f"Greatest Increase in Profits: {greatestIncrease[0]} (${int(greatestIncrease[1]):,})\n" 
    printStr += f"Greatest Decrease in Profits: {greatestDecrease[0]} (${int(greatestDecrease[1]):,})\n"

    print(printStr)

    outputfilepath = os.path.join("analysis",'analysis.txt')
    with open(outputfilepath,'w') as f:
        f.write(printStr)





