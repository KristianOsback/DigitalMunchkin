import csv

#input number you want to search
cardName = input('Enter part of name to find\n')

#read csv, and split on "," the line
csv_file = csv.reader(open('MunchkinTreasureCards.csv', "r"), delimiter=",")

#loop through the csv list
for row in csv_file:
    if len(row) > 1: #checking for empty rows
    #if current rows 2nd value is equal to input, print that row
        if cardName in row[1]:
            print(row)
        