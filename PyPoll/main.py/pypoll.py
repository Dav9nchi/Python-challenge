import os
import csv

#Set the path to the CSV file
csvpath = os.path.join('../Resources/election_data.csv')

# Set the output file path
output_path = os.path.join('../Text File/election_results.txt') 

#Initialize variables
tot_votes = 0
max_votes = 0
can_votes = {}
winner = ""

#Open the CSV file
with open(csvpath) as csvfile:

    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

        # go through every row in the file
    for row in csvreader:
        tot_votes = tot_votes + 1
        can_name = row[2]

    # Check if the candidate is in the dictionary; if not, add them with 1 vote, otherwise, increment their votes
        if can_name not in can_votes:
            can_votes[can_name] = 1
        else:
            can_votes[can_name] =can_votes[can_name] + 1

# Determine the winner and print the results to the console
print('                 Election Results')
print(f'---------------------------------------------------')
print(f'The total votes is: {tot_votes}')
print(f'---------------------------------------------------')
print("Number of votes & percentage each candidate won:")

#  through the candidate_votes dictionary to calculate percentages and find the winner
for candidate, votes in can_votes.items():
    percentage = (votes / tot_votes) * 100
    print(f'{candidate}: ({votes})votes - {percentage}%')
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# print the winner
print(f'---------------------------------------------------')
print(f'The Winner is: {winner}')
print(f'---------------------------------------------------')

# Export the results to a text file
with open(output_path, 'w') as txtfile:
    txtfile.write('                 Election Results\n')
    txtfile.write(f'---------------------------------------------------\n')
    txtfile.write(f'The total votes is: {tot_votes}\n')
    txtfile.write(f'---------------------------------------------------\n')
    txtfile.write("Number of votes & percentage each candidate won:\n")

      # go through the candidate_votes dictionary to write results to the text file
    for candidate, votes in can_votes.items():
        percentage = (votes / tot_votes) * 100
        txtfile.write(f'{candidate}: ({votes}) votes - {percentage:}%\n')
    txtfile.write(f'---------------------------------------------------\n')
    txtfile.write(f'The Winner is: {winner}\n')
    txtfile.write(f'---------------------------------------------------\n')

# Print a message indicating that the export is complete
print(f'Results exported to {output_path}')