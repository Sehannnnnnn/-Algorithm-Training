#그리디 실버1 시간관리 1263번

import sys

TC = int(input())
a = []
for _ in range(TC):
    a.append(list(map(int, sys.stdin.readline().split())))

a.sort(key=lambda x: -x[1])

time = a[0][1]
for task in a:
    t, s = task[0], task[1]
    if time <= s:
        time = time - t
    else:
        time = s - t

if time < 0:
    print(-1)
else:
    print(time)