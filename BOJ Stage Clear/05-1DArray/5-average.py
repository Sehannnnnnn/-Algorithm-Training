import sys

T = int(input())

Scores = list(map(int,sys.stdin.readline().split()))
M = max(Scores)

Scores = [score/M*100 for score in Scores]

print(sum(Scores)/T)