import sys

N, K = map(int, sys.stdin.readline().split())

a = []

for i in range(N+1):
    if i == 0:
        a.append([0 for _ in range(K+1)])
        continue
    else:
        W, V = map(int, sys.stdin.readline().split())
        for j in range(K+1):
            if j==0:
                a.append([0])
                continue
            if W <= j:
                a[i].append(max(a[i-1][j-W]+V,a[i-1][j]))
            else:
                a[i].append(a[i-1][j])

print(a[N][K])
            