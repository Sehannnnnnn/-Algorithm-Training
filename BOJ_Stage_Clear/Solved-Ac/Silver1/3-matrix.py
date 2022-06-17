# 그리디 4 행렬 1080번

import sys

n, m = map(int, sys.stdin.readline().split())
a, b = [], []
count = 0
def convertgraph(i,j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            a[x][y] = 1 - a[x][y]

for i in range(n):
    a.append(list(map(int, input())))
for i in range(n):
    b.append(list(map(int, input())))

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            convertgraph(i,j)
            count += 1

flag = 0

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            flag = 1
            break

if flag == 1:
    print(-1)
else:
    print(count)