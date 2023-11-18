
import os
import csv

#Set the path to the CSV file
csvpath = os.path.join('../Resources/budget_data.csv')

#Set the output file path
output_path = os.path.join('../Text File/financial_analysis.txt')

#Open the CSV file 
with open(csvpath) as csvfile:

    #Create a CSV reader object
    csvreader = csv.reader(csvfile)
    print(csvreader)

    #Skip the header row
    csv_header = next(csvreader)

    #Initialize variables for calculations
    total_months = 0
    total_net = 0
    changes = []
    last_value = None
    g_inc = {"date": "", "amount": float("-inf")}
    g_dec = {"date": "", "amount": float("inf")}

    # go through every row in the file
    for row in csvreader:
        total_months = total_months+1

        # Check if the row has at least 2 elements before trying to access the "Profit/Losses" value
        if len(row) >= 2:
            present_value = int(row[1])

            # Calculate the change if there was a previous value
            if last_value is not None:
                change = present_value - last_value
                changes.append(change)

                #Check for the greatest increase
                if change > g_inc["amount"]:
                    g_inc["amount"] = change
                    g_inc["date"] = row[0]

                #Check for the greatest decrease
                if change < g_dec["amount"]:
                    g_dec["amount"] = change
                    g_dec["date"] = row[0]

            total_net = total_net + present_value
            last_value = present_value
    # Calculate the average change        
    ave_change = sum(changes) / len(changes) 
    
    #Print the financial analysis results
    print('              Financial Analysis')        
    print(f'---------------------------------------------------')
    print(f'The Total number of months is: {total_months-1}')
    print(f'---------------------------------------------------')
    print(f'The Total is: ${total_net}')
    print(f'---------------------------------------------------')
    print(f'Average Change: ${ave_change}')
    print(f'---------------------------------------------------')
    print(f'Greatest Increase in Profits: {g_inc["date"]} (${g_inc["amount"]})')
    print(f'---------------------------------------------------')
    print(f'Greatest Decrease in Profits: {g_dec["date"]} (${g_dec["amount"]})')
    print(f'---------------------------------------------------')

    #Export the results to a text file
    with open(output_path, 'w') as txtfile:
        txtfile.write('[ Financial Analysis ]\n')
        txtfile.write(f'The total number of months is {total_months-1}\n')
        txtfile.write(f'The Total is: ${total_net}\n')
        txtfile.write(f'Average Change: ${ave_change}\n')
        txtfile.write(f'Greatest Increase in Profits: {g_inc["date"]} (${g_inc["amount"]})\n')
        txtfile.write(f'Greatest Decrease in Profits: {g_dec["date"]} (${g_dec["amount"]})\n')

# Print a message indicating that the export is complete
print(f'Results exported to {output_path}')