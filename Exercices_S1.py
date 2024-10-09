print("Syntax and variables")
print("=" * len("Syntax and variables"))

print("Exercise 1")
print("Hello, Python")
print("------------------------\n")



print("Exercise 2")
a = 1
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print("------------------------\n")



print("Exercise 3")
name = "Enric"
print(f"Hello {name}")
print("------------------------\n")

print("Lists and Dictionaries")
print("=" * len("Lists and Dictionaries"))

print("Exercise 4")
universities = ["UAB", "ESADE", "UOC", "IQS", "UPC"]
print(universities)
print("------------------------\n")



print("Exercise 5")
student = {
    "name": "Enric",
    "age" : 20,
    "grade" : "10"
}
for key, value in student.items():
    print(f"{key}: {value}")
print("------------------------\n")

print("Tuples and Sets")
print("=" * len("Tuples and Sets"))

print("Exercise 6")
coordinates = (10, 20)
print("Coordinates:", coordinates)
print("x:", coordinates[0])
print("y:", coordinates[1])
print("------------------------\n")



print("Exercise 7")
colors = {"red", "green", "blue"}
# Adding another color to the set
colors.add("yellow")
# Trying to add a duplicate color
colors.add("red")
# Printing the set after adding the colors
print("Colors after adding:", colors)
# Removing one color from the set
colors.pop()  
print("Colors after removing one colour:", colors)
# Creating another set and merging it
light_colors = {"white", "pink", "blue"}  
# Note "blue" is common in both sets
# Merging the two sets
merged_colors = colors.union(light_colors) 
# Printing the merged set
print("Merged set of colors:", merged_colors)

print("Control flow")
print("=" * len("Control flow"))


print("Exercise 8")
# Taking input from the user
number = float(input("Enter a number: "))
# Checking if the number is positive, negative, or zero
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")
print("------------------------\n")



print("Exercise 9")
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
print("------------------------\n")



print("Exercise 10")
number = 1
while number <= 5:
    print(number)
    number += 1
print("------------------------\n")



print("Exercise 11")
grade = input("Enter a grade (A, B, C, D, or F): ").upper()
if grade == "A":
    print("Excellent!")
elif grade == "B":
    print("Good job!")
elif grade == "C":
    print("Fair.")
elif grade == "D":
    print("Needs improvement.")
elif grade == "F":
    print("Failing.")
else:
    print("Invalid grade entered.")
print("Exercise 12")
def greet(name):
    print(f"Hello, {name}!")
print("------------------------\n")


print("Function")
print("=" * len("Function"))


print("Exercise 12")
def greet(name):
    print(f"Hello, {name}!")
greet("Enric")
print("------------------------\n")



print("Exercise 13")
def square(number):
    return number ** 2
print(square(2))
print(square(5))
print(square(10)) 
print("------------------------\n")



print("Exercise 14")
def multiply(a, b=1):
    return a * b
print(multiply(5, 3))
print(multiply(4))
print("------------------------\n")



print("Exercise 15")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 2 for number in numbers]
print(squares)
print("------------------------\n")

print("Combining all we learned")
print("=" * len("Combining all we learned"))

print("Exercise 16")
students_grades = {
    "Alice": [85, 90, 88],
    "Bob": [78, 82, 80],
    "Charlie": [92, 95, 93]
}
def print_average_grades(students_grades):
    for student, grades in students_grades.items():
        average = sum(grades) / len(grades)
        print(f"{student}'s average grade is: {average:.2f}")
print_average_grades(students_grades)
print("------------------------\n")



print("Exercise 17")
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
result = calculate(num1, num2, operator)
print("The result is:", result) 