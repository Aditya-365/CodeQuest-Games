choice1 = input("You're at a cross road, choose 'left' or 'right' : ")

if choice1 == 'left' :
    print("You have arrived at a River.")
    choice2 = input("Do you want to 'wait' or 'swim' across ")
    if choice2 == 'wait' :
        print("You have crossed the river without any harm")
        choice3 = input('''You have arrived at the 3 doors of fate. Please choose one door : 
1. 'blue' or 2. 'red' or 3. 'yellow' ''')
        if choice3 == 'blue' :
            print("The room was full of beasts.")
        elif choice3 == 'red' :
            print("The room was filled with Fire")
        else :
            print("You have found the Treasure")
    else :
        print("Crocodiles have eaten you.")
else :
    print("You have fallen into a pit. You have died. ")