
import csv
import os

bank_file = "Resources/budget_data.csv"
#bank_file = "/Users/alisha/Desktop/DataSci_Bootcamp/Homeworks/HW2_Python/PyBank/test.csv"

with open(bank_file,'r') as bankcsv:
    bank = csv.reader(bankcsv)

    next(bank) # remove header

    dates = []
    net_pf = 0
    pf_dates = {}
    gt_increase = 0
    gt_decrease = 0
    i = 0
    change = 0
    ranges = []

    for line in bank:
        date = line[0]
        pf = int(line[1])
        if date not in dates: #getting all dates
            dates.append(date)
        
        net_pf += pf # adding together profits and losses

        pf_dates[date] = pf

# Getting the greatest increase and decrease
        if i == 0 : #check if this is the first line, establish first values
            previous_date = date
            previous_pf = pf
            i += 1
        else:
            if previous_pf > pf:
                diff = previous_pf - pf
                change += (diff * -1) #changing to negative number since this is decrease
                
                if diff > gt_decrease: #comparing previous to current diff to get which is greater
                    gt_decrease = diff
                    gt_decrease_pair = []
                    gt_decrease_pair.append(date)
                    gt_decrease_pair.append(gt_decrease)

            else:
                diff = pf - previous_pf
                change += diff

                if diff > gt_increase: #comparing previous to current diff to get which is greater increase
                    gt_increase = diff
                    gt_increase_pair = []
                    gt_increase_pair.append(date)
                    gt_increase_pair.append(gt_increase)
        previous_date = date
        previous_pf = pf

    avg_change = round(change/(len(dates)-1),2)
    num = len(dates)

print("Financial Analysis")
print("-------------------------------------------")
print(f"Total Months: {num}")
print(f"Total: ${net_pf}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {gt_increase_pair[0]} (${gt_increase_pair[1]})")
print(f"Greatest Decrease in Profits: {gt_decrease_pair[0]} ($-{gt_decrease_pair[1]})")


with open("PyBank_output.txt",'w') as output:
    out = csv.writer(output, delimiter="\t")
    out.writerow(["Financial Analysis"])
    out.writerow(["-------------------------------------------"])
    out.writerow(["Total Months: " + str(num)])
    out.writerow(["Total: $" + str(net_pf)])
    out.writerow(["Average Change: $" +str(avg_change)])
    out.writerow(["Greatest Increase in Profits: " + str(gt_increase_pair[0]) + " ($" + str(gt_increase_pair[1]) +")"])
    out.writerow(["Greatest Decrease in Profits: " + str(gt_decrease_pair[0]) + " ($" + str(gt_decrease_pair[1]) +")"])


                
