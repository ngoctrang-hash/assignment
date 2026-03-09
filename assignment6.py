#Task1
numbers = []

while True:
    n = input("Enter a number: ")
    if n == "":
        break
    numbers.append(int(n))

numbers.sort(reverse=True)

print("Five greatest numbers:")
print(numbers[:5])
#Task2
seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter month (1-12): "))

if month == 12 or month == 1 or month == 2:
    print(seasons[0])
elif month >= 3 and month <= 5:
    print(seasons[1])
elif month >= 6 and month <= 8:
    print(seasons[2])
else:
    print(seasons[3])
#Task3
names = set()

while True:
    name = input("Enter name: ")
    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("Names:")
for n in names:
    print(n)
#Task4
def word_frequency(text):
    words = text.split()
    freq = {}

    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return freq


text = input("Enter text: ")
result = word_frequency(text)

print(result)
#Task5
def remove_odd(numbers):
    new_list = []

    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)

    return new_list


numbers = [1,2,3,4,5,6,7,8]

new_numbers = remove_odd(numbers)

print("Original list:", numbers)
print("Without odd numbers:", new_numbers)
#Task6
import random

N = int(input("How many points: "))

inside = 0

for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        inside += 1

pi = 4 * inside / N

print("Approximate pi:", pi)