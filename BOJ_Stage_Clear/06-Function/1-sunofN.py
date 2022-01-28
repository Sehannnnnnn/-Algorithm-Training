import sys
array = list(map(int, sys.stdin.readline().split()))

def sum(list):
    sum = 0
    for i in range(list):
        sum += i
    return sum
