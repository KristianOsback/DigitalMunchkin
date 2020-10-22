from Cards_Samlet import Cards

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
    
