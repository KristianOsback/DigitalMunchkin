from Cards_Samlet import Cards
import csv
from Print_card import PrintCard

def PickCard(cardNumber):
    
    pickedCard = ""  #variable with the specific card
    
    PrintCard()
    
    
    #read csv, and split on "," the line
    with open('MunchkinTreasureCards.csv', "r") as csv_file:
        reader = csv.reader(csv_file)

        #loop through the csv list
        for row in csv_file:
            if cardNumber == row[0]:
                if len(row) > 1: #checking for empty rows
                #Finding Card with correct cardNumber
                    pickedCard = Cards(row[0], row[2], row[3], row[17])
                    PrintCard()
            else:
                print("No card with that number")

PickCard(1)
