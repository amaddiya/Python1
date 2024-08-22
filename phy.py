# Task1
# number = int(input("Enter a number: "))
# print("You entered:", number)

# if number > 0:

#         print("The number is positive.")

#         if number % 2 == 0:

#             print("The number is even.")

#         else:

#             print("The number is odd.")

# Task2
# Get user input for the number
# number = int(input("Enter a number to generate its multiplication table: "))


# upto = int(input("Enter the range up to which the table should be generated (e.g., 10): "))

# print(f"Multiplication table for {number}:")
# for i in range(1, upto + 1):
#     print(f"{number} x {i} = {number * i}")

# Task3

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))


# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3

# print(f"The largest number is: {largest}")


# Task 4

word= input("Enter a word: ")
vowels = "aeiou"
count = 0
for char in word.lower():  
    if char in vowels:
            count += 1
print (count)





  