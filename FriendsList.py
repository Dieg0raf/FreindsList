from traceback import print_tb

# function used to display menu 
def display_Menu():
    print('-'*16)
    print("Menu".center(16))
    print('-'*16)
    print("1: Add friend")
    print("2: Delete Friend")
    print("3: Change name of Friend")
    print("4: Search friend by name")
    print("5: Show Friends List")
    print("6: Exit")

# function used to display Friends List
def print_friendsList(List):
    i = 0
    for name in List:
            i += 1
            print(f"{i}: {name}")
    print()

# function used to ouput the choice the user chose
def menu_Option(userChoice, List):
    # if user enter 1
    if(userChoice == 1):
        print('-'*30)
        friend = input("Add friend name: ") # name of the new Friend that is going to be added to Friends List
        print()
        List.append(friend) # Friend is appended to the end of the list
        print(f"\'{friend}\' has been added to your Friends List.")
        print()
    # if user enters 2
    elif(userChoice == 2):
        print('-'*30)
        deleteName = input("Delete Name: ") # name of Friend that you user wants to delete
        print()
        for i in range(len(List)):
            if(List[i] == deleteName):
                List.remove(deleteName)
                print(f"\'{deleteName}\' has been deleted from your Friends List.") # if Friend is found it prints this message
                notThere = True
                print()
                break
            else:
                notThere = False
        if(notThere == False):
            print(f"\'{deleteName}\' does not exist on your Friends List. (Try again)")
    
    # if user enters 3
    elif(userChoice == 3):
        changeName = input("Name of the friend you want to change: ") # name wanting to change
        newName = input("New Name: ") # new name that is going to be given in place of the old name
        # checks through list to find the name of the user
        for i in range(len(List)):
            if(List[i] == changeName):
                List[i] = newName
                print(f"\'{changeName}\'s name has been changed to \'{newName}\'.") # if found it will change and output this message
                notThere = True
                print()
                break
            else:
                notThere = False
        if(notThere == False):
            print(f"\'{changeName}\' does not exist on your Friends List. (Try again)")
            print() # if not found it will outpout this message and ask to retry
    
    # if user enters 4 
    elif(userChoice == 4):
        print('-'*30)
        searchName = input("Search Name: ") # name wanted to search in Friends List
        print()
        # checks to see if name of Friend is or is not on the Friends List
        if searchName in List:
            print(f"\'{searchName}\' is on your Friends List.")
        else:
            print(f"\'{searchName}\' is not on your Friends List.")
    
    # if user enter 5
    elif(userChoice == 5):
        print('-'*26)
        print("Friends List") # Freinds list is outputed
        print('-'*26)
        print_friendsList(List) # call function which prints out Friends List
    
    # if user enters 6
    elif(userChoice == 6):
        print('-'*26)
        print("Friends List".center(26)) # Freinds List is outputed onto screen
        print('-'*26)
        if(len(List) == 0):
            print("You have no Freinds LOL") # if no Friends this message outputs
            print()
        else:
            print_friendsList(List)
        print("Thank you for making your Freinds List with my program")

# Display of the starting screen
print('-'*35)
print("Welcome to making your freinds list")
print('-'*35)
print("Enter the letter \'M\' to enter the Menu")
letter = input("Enter: ")
letter = letter.upper()

# checks to see if user enters the correct letter
print()
if(letter != 'M'):
    while(letter != 'M'): # keeps asking user to enter "M" to be able to advance
        print("Please only enter the letter \'M\'")
        letter = input("Enter: ")
        letter = letter.upper()

# List used to keep friends
friendList = []

# prints out the menu for the program
if(letter == 'M'):
    display_Menu()
    userChoice = int(input("Choose an option (1-6): "))
    menu_Option(userChoice,friendList)
    while (userChoice != 6):
        display_Menu()
        userChoice = int(input("Choose an option (1-6): "))
        menu_Option(userChoice,friendList)
