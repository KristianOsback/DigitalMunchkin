import csv

#input number you want to search
cardName = input('Enter part of name to find\n')

#read csv, and split on "," the line
csv_file = csv.reader(open('MunchkinTreasureCards.csv', "r"), delimiter=",")

#result of search list variables
searchResult = []

#loop through the csv list
for row in csv_file:
    if len(row) > 1: #checking for empty rows
    #if input is equel to anything in the file, then it is returned. lower() makes sure it does not distinguish between lower and uppercase. 
        if any(cardName.lower() in cell.lower() for cell in row):
            searchResult.append(row) #adding row to result 
#Throws a message when nothing is found.
if len(searchResult) == 0:
    print("No hits!")
else: #printing each result on a new line
    for row in searchResult:
        print(row)
    print(f"\n {len(searchResult)} results found") #counting the results
    
    
"""
where should with be be placed?
Does not work on all rowes. Eg inside the {}. 
"""
