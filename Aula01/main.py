print("Welcome to the game")
print("1. Go to the house")
print("2. Go to the forest")
print("3. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("The house has a sword")
    print("1. Take the sword")
    print("2. Ignore the sword")
    print("3. Get back to the forest")
    sword = int(input("Enter your choice: "))
    if sword == 1:
        print("The player claimed a sword")
    elif sword == 2:
        print("Your inventory is empty!")
    elif sword == 3:
        print("You were eaten by a bear, try again!")
    else :
        print("Invalid choice")
elif choice == 2:
    print("The forest is dark")
