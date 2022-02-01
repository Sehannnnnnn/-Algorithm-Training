#silver 3 1448번 그리디

N = int(input())
a = []

for _ in range(N):
    a.append(int(input()))

a = sorted(a, reverse=True)

d = {}

for i, x in enumerate(a):
    for j, y in enumerate(a):
        if i == j:
            continue
        for k, z in enumerate(a):
            if i == k or j == k:
                continue
            d[x+y+z] = [x,y,z]

sorted_d = sorted(d.items(),reverse=True)

def makeTriangle(d):
    for triangle in sorted_d:
        if triangle[1][2] < triangle[1][0] + triangle[1][1]:
            return triangle[0]
        continue
    return -1

print(makeTriangle(sorted_d))

## 실패 -> 어짜피 a>b+c 이면 bc 보다 작은거는 만족 못함

import sys
t = int(input())
s = []
for i in range(t):
    s.append(int(sys.stdin.readline()))
s.sort(reverse=True)
istrue = False
for i in range(len(s) - 2):
    if s[i] < s[i + 1] + s[i + 2]:
        print(s[i] + s[i + 1] + s[i + 2])
        istrue = True
        break
if istrue == False:
    print(-1)