#task1
name = input("What your name: ")
print(f"Hello, {name}!")
#task2
import math

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference of the circle is {circumference:.2f}")
#task3
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
area = length * width

print(f"Perimeter: {perimeter}")
print(f"Area: {area}")
#task4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

total = a + b + c
product = a * b * c
average = total / 3

print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average}")
#task5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_lots = talents * 20 * 32 + pounds * 32 + lots
total_grams = total_lots * 13.3

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")