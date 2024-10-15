from pathlib import Path

#Define path to the files
path_customers = Path("customer.txt")
path_books = Path("books.txt")

print("1. Register a new customer")
print("2. Register a new book")

choice = input("Enter your choice: ")

if choice == "1":
    #Generate Card Number
    try:
        with path_customers.open() as f:
            line = f.readlines()
            card_num = len(line)
    except FileNotFoundError:
        card_num = 1

    #Request customer information
    name = input("Write your name: ")
    tel = input("Write your telephone number: ")

    #Open file in the "a" (append) mode
    with path_customers.open(mode="a") as f:
        f.write(f"Name: {name}\nTelephone number: {tel}\nID Number: {card_num}\n" + "\n")

    print(f"Client registered successfully! Your card number is: {card_num}")
elif choice == "2":
    try:
        with path_books.open() as f:
            line = f.readlines()
            id_num = len(line)
    except FileNotFoundError:
        id_num = 1

    # Request customer information
    name = input("Write the book's name: ")

    # Open file in the "a" (append) mode
    with path_books.open(mode="a") as f:
        f.write(f"Name: {name}\nID Number: {id_num}\n" + "\n")

    print(f"Book registered successfully! Book's id number is: {id_num}")
else:
    print("Invalid choice. Please try again.")