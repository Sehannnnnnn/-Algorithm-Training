import sys
import math

def dist(dot1, dot2):
    distance = math.sqrt((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2)
    return distance


def dist_c(dot1, dots):
    arr = []
    for i in range(len(dots)):
        arr.append(dist(dot1, dots[i]))
    return min(arr)

n, k = map(int, input().split())

arr = []

for i in range(n):
    arr.append((list(map(int, sys.stdin.readline().split()))))
    arr[i].append(i)


c = []

c.append(arr[0])
for j in range(1, k):
    d = []
    for i in range(len(arr)):
        if arr[i] in c:
            d.append(0)
            # print('넘어갔음. arr[i] : ', arr[i], 'c: ',c)
            pass
        else:
            d.append(dist_c(arr[i],c))
            # print('j:', j , 'i:',i)
            # print('max(d):', max(d), 'max(d)의 index: ', d.index(max(d)),'\n')
    c.append(arr[d.index(max(d))])


arr.sort(lambda x : x[2])

for _ in c:
    print(_[0], _[1])
 