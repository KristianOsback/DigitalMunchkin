def PrintCard():
    
    temp_var = []
    indent = 30
    indent2 = 32

    cardNumber = str(6)
    cardName = "Transferral Potion"
    cardDescription = "Quick transportation"

    print(" " + "".center(indent2, '-')) #printing top
    
    #printing cardNumber
    print("".center(0, ' '), end=" ")
    print("|", end=" ") #Printing left side
    print("6", end=" ") #Printing cardNumber
    print("|".rjust(indent - (len(cardNumber) + 1), " ")) #Printing right side
    
    #Printing empty space
    for i in range(1):
        print("".center(0, ' '), end=" ")
        print("|", end=" ") #Printing left side
        print("|".rjust((indent), " ")) #Printing right side
    
    #printing cardName
    print("".center(0, ' '), end=" ")
    print("|", end=" ") #Printing left side
    print(cardName.center((indent - len(cardName)), " "), end=" ") #Printing cardNumber
    print("|".rjust(indent - (len(cardName) + 1), " ")) #Printing right side
    
    #Printing empty space
    for i in range(5):
        print("".center(0, ' '), end=" ")
        print("|", end=" ") #Printing left side
        print("|".rjust((indent), " ")) #Printing right side
    
    #printing cardDescription
    print("".center(0, ' '), end=" ")
    print("|", end=" ") #Printing left side
    print(cardDescription.center((indent - len(cardDescription)), " "), end=" ") #Printing cardNumber
    print("|".rjust(indent - (len(cardDescription) + 1), " ")) #Printing right side

    #Printing empty space
    for i in range(10):
        print("".center(0, ' '), end=" ")
        print("|", end=" ") #Printing left side
        print("|".rjust((indent), " ")) #Printing right side
    
    print(" " + "".center(indent2, '-')) #Printing bottom

PrintCard()