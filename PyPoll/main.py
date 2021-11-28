#Import dedpendencies
import csv
import os

#import csv file
csvpath = os.path.join("Resources", "election_data.csv")

#create three different lists to capture candidate's names, each candidtae's total votes and vote percentage for each candidate
Candidates=[]
Number_of_votes=[]
Vote_Percentage=[]

#Assign variable to start 
total_votes=0

#Open and read the data
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #loop through each row in election_data csv file
    for row in csvreader:

        #Keep adding the vote counter as we go through the loop.
        total_votes=total_votes+1

        candidate_name = row[2]

        #Run if fuction to capture candidate names and to get the total votes.
        #if anyone's name not in my Candiddate list add their name into the list using "append" and add their votes into "Number_of_votes" list

        if candidate_name not in Candidates:
            Candidates.append(candidate_name)

            index=Candidates.index(candidate_name)
            Number_of_votes.append(1)

        #if the candidate name is already in my Candidate list, just add their votes into the number of vote list
        else:
            index=Candidates.index(candidate_name)
            Number_of_votes[index]+=1

    #Run another for loop to calculate the Vote percentages and find the winner
    for votes in Number_of_votes:
        percentage=round((votes/total_votes)*100)
        #maintain the percentage decimal places upto 3 decimals.
        percentage = "%.3f%%" % percentage
        #add the percentage into Vote_Percentage list
        Vote_Percentage.append(percentage)

    #find who won the election, who recieved highest number of votes according to the Number_of_votes list
    Winner=max(Number_of_votes)
    index= Number_of_votes.index(Winner)
    Winning_Candidate=Candidates[index]


# print the results in the terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(Vote_Percentage[i])} ({str(Number_of_votes[i])})")
print("--------------------------")
print(f"Winner: {Winning_Candidate}")
print("--------------------------")


# Exporting results into .txt file
output = open("Analysis.txt", "w")

line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(Candidates)):
    line = str(f"{Candidates[i]}: {str(Vote_Percentage[i])} ({str(Number_of_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {Winning_Candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))




