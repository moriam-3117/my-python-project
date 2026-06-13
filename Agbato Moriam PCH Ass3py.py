#sum it up: write a loop that calculates the sum of numbers from 1 to 100
total = 0

for i in range(1, 101):
    total = total + i

print("The sum is:", total)

#count evens: print all even numbers between 1 and 50 using a for loop
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#Reverse it: take a number 347952 and print it backwards using a while loop
number = 347952

while number > 0:
    digit = number % 10
    print(digit, end="")
    number = number // 10


#star pattern : print triangle using nested loops
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()