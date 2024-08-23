def greet(name):

    print(f"Hello, {name}")
greet("Ahmad")

def greet (first_name, last_name ="Rahmani"):
    print(f"Hello, {last_name} {first_name}")

greet("kamal , Ahmad")

def multiply (a, b):
    return a * b
print (multiply(5, 6))

fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
fruits.remove("banana")
fruits.insert(1, "blueberry")
fruits.sort()
print(fruits)


for number in range(1, 11):
    if number == 7:
        break
    print(number)

for number in range(1, 11):
    if number % 3 == 0:
        continue
    print(number)
