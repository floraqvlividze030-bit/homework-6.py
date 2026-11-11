# Task 1.1 – Squares of numbers

for count in range(1, 11):
    n = count ** 2
    print(count,"squared =", n)

for count in range(10, 0, -1):
        print(count)
print("Go!")

total = 0

for num in range(1, 101):
    if num % 2 == 0:
        total += num
print("Sum of even numbers:", total)

# Task 2 - Ount Vowels

ch = input("Enter a text: ")
count = 0

for text in ch:
    if text in "aeiou":
        count += 1

print("Number of vowels:", count)

# Task 3 Sum of Numbers using continue

total = 0

while True:
    num = input("Enter a number or stop: ")

    if num == "stop":
        break

    num = int(num)

    if num < 0:
        continue

    total += num

print("Sum:", total)

# Task 4  Nested Loops

for row in range(5):
    for col in range(row + 1):
        print("*", end=" ")
    print()

for row in range(5, 0, -1):
    for col in range(row):
        print("*", end=" ")
    print()