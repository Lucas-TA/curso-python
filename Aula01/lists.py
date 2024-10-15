#lists

#string
# fruits = ['Apple', 'Banana', 'Strawberry']
# print("Fruit: ", fruits[1])
# fruits.append('Mango')
# print(fruits)
#
# for fruit in range(len(fruits)):
#     print(fruits[fruit])


#numbers
# numbers = [1, 2, 3, 4, 5]
# numbers[1] = 0
# print(numbers[1])
# numbers.remove(4)
# print(numbers)

#mix
# mix = [1, 'banana', 3.5, True]

# name = input('Qual o seu nome? ')
# print(f"Hello, {name}, Welcome!")

fruits = []
while True:
    fruit = input("Qual a sua fruit? Or quit ")
    if fruit.lower() == 'quit' :
        break
    fruits.append(fruit)

    print("fruits list")
    for fruit in fruits:
        print(fruit)