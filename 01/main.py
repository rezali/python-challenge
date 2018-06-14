import os
import csv

csvpath = os.path.join("raw_data", "budget_data_1.csv")


with open(csvpath, newline="") as csvfile:
        
        #csvreader specifies delimiter
        csvreader = csv.reader(csvfile, delimiter=",")
        
        #the first line is the header
        header = next(csvreader)
        revenue = []
        months = []

        for row in csvreader:
            revenue.append(float(row[1]))
            revsum = round(sum(revenue), 0)
            months.append(row[0]) 
            moncount = len(months)
            revavg = round(float(revsum / moncount), 2)
            revchange = [x - revenue[i - 1] for i, x in enumerate(revenue)][1:]
            
            def min_max(revchange):
                return min(revchange), max(revchange)

print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(moncount))
print("Total Revenue: " + "$ " + str(revsum))
print("Average Revenue Change: " + "($ " + str(revavg) +")")
print("Greatest Decrease in Revenue: " + "($ " + str(min(revchange)) +")")
             
output_path = os.path.join("raw_data", "finalbank1.txt")
with open(output_path, "w") as output_file:
    output_file.write( f'Financial Analysis = {finalbank1.txt} \n')



    

        



            
            
            

            
        
    