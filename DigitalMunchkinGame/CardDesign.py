from Cards_Samlet import Cards

def PickCard(cardNumber):
    
    pickedCard #variable with the specific card

    #read csv, and split on "," the line
    csv_file = csv.reader(open('MunchkinTreasureCards.csv', "r"), delimiter=",")

    #loop through the csv list
    for row in csv_file:
        if len(row) > 1: #checking for empty rows
            #Finding Card with correct cardNumber
            if cardNumber == row[0]:
                pickedCard = Cards(row[0], row[2], row[3], row[17])
            else:
                print("No card with that number")

    temp_var = []
    indent = 30
    indent2 = 32
    def PrintCard():
        print(" " + "".center(indent2, '-')) #printing top
        for i in range(20):
            print("".center(0, ' '), end=" ")
            print("|", end=" ")
            print("|".rjust(indent, " ")) 
        print(" " + "".center(indent2, '-'))

PickCard(1)