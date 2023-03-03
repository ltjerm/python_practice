##### WOrking with lists ########

pokemon = ['pikachu', 'charmander', 'squirtle', 'bulbasaur']

# for p in pokemon: 
#     print(f"{p.title()} is a pokemon") 
#     print(f"I cant wait to catch a {p.title()}")

# print("All of these pokemon are cool!")

##Try it yourself 4-1
pizza = ['pepperoni', 'cheese', 'sausage', 'mushroom']
# for p in pizza:
    # print(p)
#     print(f" I like {p} pizza")
# print("I really like pizza!")

# animals = ['dog', 'cat', 'bird', 'fish']

# for a in animals:
#     print(f"A {a} would make a great pet")

# print("Any of these animals would make a great pet")

# for i in range(10):
#     print(i)


# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# odd_numbers =list(range(1,11,2))
# print(odd_numbers)

# random = list(range(0,100,5))
# print(random)

# square = []
# for value in range(1,20):
#     square.append(value**2)
# print(square)


# triangle = []
# for value in range(1,11):
#     triangle.append(value**3)

# print(triangle)

# colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

# for color in colors:
#     print(color)

# cars = []

# for car in range(0,10):
#     cars.append(car)

# print(cars)

digits = [1,2,3,4,5,6,7,8,9,0]

print(min(digits))
print(max(digits))
print(sum(digits))


######### List Comprehensions #########

square = [value*2 for value in range(1,11)]
print(square)

numero = [code**3 for code in range(1,11)]
print(numero)

