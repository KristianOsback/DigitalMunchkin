def PrintCard():
    
    temp_var = []
    indent = 25
    indent2 = 27

    cardNumber = str(6)
    cardName = "Transferral Potion"
    cardType = "Item"
    cardDescription = "Quick transportation"
    isBig = True
    itemValue = str(300)

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
    
    #printing cardType
    print("".center(0, ' '), end=" ")
    print("|", end=" ") #Printing left side
    print(cardType.center((indent - len(cardType)), " "), end=" ") #Printing cardNumber
    print("|".rjust(indent - (len(cardType) + 18), " ")) #Printing right side
    
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
    for i in range(8):
        print("".center(0, ' '), end=" ")
        print("|", end=" ") #Printing left side
        print("|".rjust((indent), " ")) #Printing right side
    
 
    #printing Big and itemValue
    print("".center(0, ' '), end=" ")
    print("|", end=" ") #Printing left side
    print(itemValue.rjust((indent - 20), " "), end=" ") #Printing cardNumber
    if isBig == True:
        print("Big".rjust((indent -(len(itemValue) + 5)), " "), end=" ") #Printing cardNumber
    print("|".rjust(indent - (len(itemValue) + 21), " ")) #Printing right side
        
    print(" " + "".center(indent2, '-')) #Printing bottom
    
    
    
    

"""
- What determines how many spaces you need to take out to make space for text?
- Why does .center not work with long strings?
- Why does .rjust not work with Big
"""
PrintCard()