#loop, for, in, range, #while
# times = int(input("How many times you want it to repeat? "))

# fruits = ["Apple", "Banana", "Strawberry"]
#
# for fruit in fruits:
#     print(fruit)
#
# for i in range(5):
#     print(i)
#
# for i in range(1, 11):
#     print(i)
#
# for i in range(0, 11, 2):
#     print(i)

# counter = 10
# while counter <= 11:
#     print(counter)
#     counter += 1

# while counter > 0:
#     print(counter)
#     counter -= 1
# print('Happy birthday!')

correct_password = "123"
written_password = ''

print("Welcome! Please, write your password.")

while written_password != correct_password:
    written_password = input("Write your password: ")
    if written_password == correct_password:
        print("Correct!")
        break
print("Access allowed")