import csv

#input number you want to search
cardName = input('Enter part of name to find\n')

#read csv, and split on "," the line
csv_file = csv.reader(open('MunchkinTreasureCards.csv', "r"), delimiter=",")

#result of search list
searchResult = []

#loop through the csv list
for row in csv_file:
    if len(row) > 1: #checking for empty rows
    #if input is equel to anything in the file, then it is returned. lower() makes sure it does not distinguish between lower and uppercase. 
        if cardName.lower() in map(lambda x:x.lower(),row) or cardName.lower() in row[1].lower():
            searchResult.append(row)

if len(searchResult) == 0:
    print("No hits!")
else:
    for row in searchResult:
        print(row)
    print(f"\n {len(searchResult)} results found")
"""
Nothing found if no cards is found
No difference of lowercase and uppercase
where should with be be placed?
map(lambda x:x.lower(),["A","B","C"])
"""
