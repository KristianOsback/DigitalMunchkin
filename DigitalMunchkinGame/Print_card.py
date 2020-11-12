def PrintCard():
    
    temp_var = []
    indent = 25
    indent2 = 27

    cardNumber = str(6)
    cardName = "Transferral Potion"
    cardType = "Item"
    cardDescription = "Quick transportation"
    isBig = False
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
    print("|", end="") #Printing left side remove space in end
    print(cardName.center((indent), " "), end="") #Printing cardNumber - remove the space in end and the extra indent.
    print("|") #Printing right side, only the line
    
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
    print("|", end="") #Printing left side
    print(cardDescription.center((indent), " "), end="") #Printing cardNumber
    print("|") #Printing right side

    #Printing empty space
    for i in range(8):
        print("".center(0, ' '), end=" ")
        print("|", end=" ") #Printing left side
        print("|".rjust((indent), " ")) #Printing right side
    
 
    #printing Big and itemValue
    print("".center(0, ' '), end=" ")
    print("|", end="") #Printing left side
    print(itemValue, end="") #Printing cardNumber
    if isBig == True:
        print("Big".rjust((indent-3), " "), end="") #Printing Big
        print("|") #Printing right side
        print(" " + "".center(indent2, '-')) #Printing bottom
    else:
        print(" ".rjust((indent-3), " "), end="") #Printing Big
        print("|") #Printing right side
        print(" " + "".center(indent2, '-')) #Printing bottom
        
    
    
    
    
    

PrintCard()