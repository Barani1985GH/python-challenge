# Modules
import os
import csv

# Declare a List variable to store all financial record as dictionary
financial_rec = []  # To store all records inside a list
total_amount = 0    # To store total profit/loss over the entire period
just_profit_loss = []   # To store all the profit/losses in a list manupulation
just_dates = [] # To store all the dates in a list for manupulation
changes = []    # To store the profit/loss changes over the entire period 
j = 1   # To iterate through for loop

# Set path to csv file
csvpath = os.path.join("Resources", "budget_data.csv")
# set path to txt file
analysispath = os.path.join("Analysis","analysis.txt")

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    
    #calculate total month
    for row in csvreader:
        financial_rec.append(row) 
    
    #calculate total profit/loss
    for record in financial_rec:
        total_amount = total_amount + int(record["Profit/Losses"])
        just_profit_loss.append(record["Profit/Losses"]) 
        just_dates.append(record["Date"])    
    
    #calculate changes in profit/loss
    for i in range(len(just_profit_loss)): # length of just_profit_loss = 86, set range  = 0 to 85
       if(j<(len(just_profit_loss))):
            difference = int(just_profit_loss[j]) - int(just_profit_loss[i])
            changes.append(difference)
            j = j+1

    print("\nFinancial Analysis\n\n----------------------------")
    
    #The total number of months included in the dataset
    print ("\nTotal Months: ",len(financial_rec) )

    #The net total amount of "Profit/Losses" over the entire period
    print ("\nTotal amount: $",total_amount )  
    
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes   
    print ("\nAverage Change : $",round((sum(changes)/len(changes)),2))  # using sum() & len() calculate average of total changes
      
    #The greatest increase in profits (date and amount) over the entire period
    print ("\nGreatest Increase in Profits: ", just_dates[(changes.index(max(changes)))+1], "($",max(changes),")")  # used max & min value list index to capture their dates 
    
    #The greatest decrease in profits (date and amount) over the entire period
    print ("\nGreatest Increase in Profits: ",just_dates[(changes.index(min(changes)))+1]," ($",min(changes), ")\n" )   
   
    analysis = ['\nFinancial Analysis\n\n----------------------------\nTotal Months: ',len(financial_rec),"\n\nTotal amount: $",total_amount,"\n\nAverage Change : $",round((sum(changes)/len(changes)),2),"\n\nGreatest Increase in Profits: ", just_dates[(changes.index(max(changes)))+1], " ($",max(changes),")\n\nGreatest Increase in Profits: ",just_dates[(changes.index(min(changes)))+1]," ($",min(changes), ")\n"]
    
# write analysis to txt file
with open(analysispath,'w') as file:
    for i in analysis:
     file.write(str(i))



