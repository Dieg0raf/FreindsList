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
    if(userChoice == 1):
        print('-'*30)
        friend = input("Add friend name: ")
        print()
        List.append(friend)
        print(f"\'{friend}\' has been added to your Friends List.")
        print()
    elif(userChoice == 2):
        print('-'*30)
        deleteName = input("Delete Name: ")
        print()
        List.remove(deleteName)
        print(f"\'{deleteName}\' has been deleted from your Friends List.")
        print()
    
    # come back to this problem !
    elif(userChoice == 3):
        changeName = input("Name of the friend you want to change: ")
        newName = input("New Name: ")
        for i in range(len(List)):
            if(list[i] == changeName):
                list[i] = newName
                print(f"\'{changeName}\'s name has been changed to \'{newName}\'.")
                print()
                break
    elif(userChoice == 4):
        print('-'*30)
        searchName = input("Search Name: ")
        print()
        if searchName in List:
            print(f"\'{searchName}\' is already on your Friends List.")
        else:
            print(f"\'{searchName}\' is not on your Friends List.")
    elif(userChoice == 5):
        print('-'*26)
        print("Friends List")
        print('-'*26)
        print_friendsList(List)
    elif(userChoice == 6):
        print('-'*26)
        print("Friends List".center(26))
        print('-'*26)
        if(len(List) == 0):
            print("You have no Freinds LOL")
            print()
        else:
            print_friendsList()
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
