import sys

T = int(input())
numbers = str(input())
sum = 0

for number in numbers:
    number = int(number)
    sum += number

print(sum)  