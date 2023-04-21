import os
import csv

pybank_path = os.path.join('Resources', 'budget_data.csv')
createfilepath =  os.path.join('analysis', 'PyBankanalysis.txt')


TotalMonths = 0
Profit_Losses = 0
Average = 0
GreatIncrease = 0
GreatDecrease = 0
IndTotals = []


with open(pybank_path, 'r') as pybank_data:

	csvreader = csv.reader(pybank_data,delimiter=",")
	
	next(csvreader)
	beginningrow = next(csvreader)
	lastcell = float(beginningrow[1])
	IndTotals.append(0)
	TotalMonths += 1
	Profit_Losses += lastcell
	maxmonth = beginningrow[0]
	minmonth = beginningrow[0]
	max_total = 0
	min_total = 0

	for row in csvreader:

		PL = float(row[1])
		month = row[0]
		PLTotal = PL - lastcell
		IndTotals.append(PLTotal)
		lastcell = PL
		TotalMonths += 1
		Profit_Losses += PL

		if PLTotal > max_total:
			max_total = PLTotal
			maxmonth = month
		
		if PLTotal < min_total:
			min_total = PLTotal
			minmonth = month

if lastcell:
	average = round(sum(IndTotals) / (len(IndTotals)-1), 2)

print(" " + "\n")
print("Financial Analysis\n")
print("----------------------------\n")
print("Total Months: " + str(TotalMonths) + "\n")
print("Total: $" + str(round(Profit_Losses))+ "\n")
print("Average Change: $" + str(average)+ "\n")
print("Greatest Increase in Profits: " + maxmonth + " ($" + str(round(max_total)) + ")"+ "\n")
print("Greatest Decrease in Profits: " + minmonth + " ($" + str(round(min_total)) + ")"+ "\n")

with open(createfilepath, "w") as f:
	f.write(" " + "\n")
	f.write("Financial Analysis\n")
	f.write(" " + "\n")
	f.write("----------------------------\n")
	f.write(" " + "\n")
	f.write("Total Months: " + str(TotalMonths) + "\n")
	f.write(" " + "\n")
	f.write("Total: $" + str(round(Profit_Losses))+ "\n")
	f.write(" " + "\n")
	f.write("Average Change: $" + str(average)+ "\n")
	f.write(" " + "\n")
	f.write("Greatest Increase in Profits: " + maxmonth + " ($" + str(round(max_total)) + ")"+ "\n")
	f.write(" " + "\n")
	f.write("Greatest Decrease in Profits: " + minmonth + " ($" + str(round(min_total)) + ")"+ "\n")