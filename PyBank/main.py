#Import dedpendencies
import os
import csv

# #import csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#Just checking the path is working before go ahead & commented after checking as it is not part of assignment
#print(csvpath)

#Creating empty lists for months, revenue and monthly Profit/loss changes
Total_months=[]
Total_revenue=[]
Monthly_P_change=[]

# Open & Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row
    csv_header=next(csvreader)

    #Iterate through each row in budget_data csv file
    for row in csvreader:
    
        #Add months and the total revenue into their corresponding lists (months should start adding into list from index 0 while revenue starts from second position, mean index 1)
        Total_months.append(row[0])
        Total_revenue.append(int(row[1]))  

    #Iterate through the Revenue list to calculate the monthly revenue Change. 
    for x in range(len(Total_revenue)-1):
        
        #Calculate the monthly change by taking the difference between two months and add them into a list
        Monthly_P_change.append(Total_revenue[x+1]-Total_revenue[x])

#Locate the Max and Min Revenue change Value from revenue change list
Max_Rev_increase_value=max(Monthly_P_change)
Min_Rev_decrease_value=min(Monthly_P_change)

#find the Max and Min Revenue Value change date
Max_Rev_increase_date=Monthly_P_change.index(max(Monthly_P_change))+1
Min_Rev_increase_date=Monthly_P_change.index(min(Monthly_P_change))+1

# Print Statements into terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Total_months)}")
print(f"Total: ${sum(Total_revenue)}")
print(f"Average Change: {round(sum(Monthly_P_change)/len(Monthly_P_change),2)}")
print(f"Greatest Increase in Profits: {Total_months[Max_Rev_increase_date]} (${(str(Max_Rev_increase_value))})")
print(f"Greatest Decrease in Profits: {Total_months[Min_Rev_increase_date]} (${(str(Min_Rev_decrease_value))})")


#Export results into .txt file
output = open("Analysis.txt", "w")

   
# Write methods to print to Financial_Analysis_Summary 
line1 =("Financial Analysis")
  
line2 =("----------------------------")
   
line3 =(f"Total Months: {len(Total_months)}")
   
line4 =(f"Total: ${sum(Total_revenue)}")
 
line5 =(f"Average Change: {round(sum(Monthly_P_change)/len(Monthly_P_change),2)}")
    
line6 =(f"Greatest Increase in Profits: {Total_months[Max_Rev_increase_date]} (${(str(Max_Rev_increase_value))})")
  
line7 =(f"Greatest Decrease in Profits: {Total_months[Min_Rev_increase_date]} (${(str(Min_Rev_decrease_value))})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))

