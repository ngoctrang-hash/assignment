i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1


while True:
    inch = float(input("Enter inches (negative number to quit): "))

    if inch < 0:
        print("Program ended.")
        break

    cm = inch * 2.54
    print(inch, "inches =", cm, "cm")


numbers = []

while True:
    user_input = input("Enter a number (press Enter to quit): ")


    if user_input == "":
        break

    numbers.append(float(user_input))

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers.")


import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct!")
        break


correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Wrong credentials")
        attempts += 1

if attempts == 5:
    print("Access denied")


def middle_character(text):
    length = len(text)
    middle = length // 2

    if length % 2 == 0:
        return text[middle - 1:middle + 1]
    else:
        return text[middle]


def acronym(phrase):
    words = phrase.split()
    result = ""

    for word in words:
        result += word[0].upper()

    return result
