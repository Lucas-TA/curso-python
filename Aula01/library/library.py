from pathlib import Path

path = Path("customer_library.txt")

data = []

name = input("Write your name: ")
tel = input("Write your telephone number: ")
card_number = input("Write your card number: ")

filled_data = f"Name: {name}\nTelephone number: {tel}\nCard Number: {card_number}\n"
data.append(filled_data)

with path.open(mode="a") as f:
    f.write(filled_data + "\n")

print("Registered successfully")

for record in data:
    print(record)