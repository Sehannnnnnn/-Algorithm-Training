import sys
import math

def input():
    return sys.stdin.readline().strip()

coins = list(map(int, input().split(', ')))
money = int(input())

C = [math.inf]*(money+1)
C[0] = 0
for j in range(1,money+1):
    for i in range(len(coins)):
        if coins[i] <= j and C[j-coins[i]]+1 < C[j]:
            C[j] = C[j-coins[i]]+1
        else:
            pass

print(C[money])
