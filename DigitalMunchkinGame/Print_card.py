from SearchFunction_v2 import return_card, print_card

card = return_card()



def PrintCard(CardItem):

    indent = 25
    indent2 = 27

    card.cardNumber = CardItem.cardNumber
    card.cardName = CardItem.cardName
    card.cardType = "Treasure"
    card.cardDescription = CardItem.cardDescription
    card.isBig = CardItem.big
    card.value = 100

    print(" " + "".center(indent2, '-'))  # printing top
    
    # printing cardNumber
    print("".center(0, ' '), end=" ")
    print("|", end=" ")        # Printing left side
    print("6", end=" ")      # Printing cardNumber
    print("|".rjust(indent - (len(card.cardNumber) + 1), " ")) # Printing right side
    
    # Printing empty space
    for i in range(1):
        print("".center(0, ' '), end=" ")
        print("|", end=" ")   # Printing left side
        print("|".rjust((indent), " "))  # Printing right side
    
    # printing cardName
    print("".center(0, ' '), end=" ")
    print("|", end="") # Printing left side remove space in end
    print(card.cardName.center((indent), " "), end="") # Printing cardNumber - remove the space in end and the extra indent.
    print("|")  # Printing right side, only the line
    
    # printing cardType
    print("".center(0, ' '), end=" ")
    print("|", end="") # Printing left side
    print(card.cardType.center((indent), " "), end="") # Printing cardNumber
    print("|")  # Printing right side
    
    # Printing empty space
    for i in range(5):
        print("".center(0, ' '), end=" ")
        print("|", end=" ") # Printing left side
        print("|".rjust((indent), " ")) # Printing right side
    
    # printing cardDescription
    print("".center(0, ' '), end=" ")
    print("|", end="")  # Printing left side
    print(card.cardDescription.center((indent), " "), end="") # Printing cardNumber
    print("|")  # Printing right side

    # Printing empty space
    for i in range(8):
        print("".center(0, ' '), end=" ")
        print("|", end=" ") # Printing left side
        print("|".rjust((indent), " ")) # Printing right side

    # printing Big and itemValue
    print("".center(0, ' '), end=" ")
    print("|", end="") # Printing left side
    print(card.value, end="") # Printing cardNumber
    if card.isBig == "Big":
        print("Big".rjust((indent-3), " "), end="")  # Printing Big
        print("|")  # Printing right side
        print(" " + "".center(indent2, '-')) # Printing bottom
    else:
        print(" ".rjust((indent-3), " "), end="")  # Printing Big
        print("|")  # Printing right side
        print(" " + "".center(indent2, '-'))  # Printing bottom
        
PrintCard(card)
  # Search for staff for best result



