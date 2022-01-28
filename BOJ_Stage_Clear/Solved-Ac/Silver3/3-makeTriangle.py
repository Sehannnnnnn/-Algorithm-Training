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