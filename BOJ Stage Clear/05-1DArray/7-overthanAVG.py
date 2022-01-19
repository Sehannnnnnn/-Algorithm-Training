import sys

C = int(input())

for _ in range(C):
    case = list(map(int, sys.stdin.readline().split()))
    AVG = sum(case[1:])/case[0]
    upAVG = []
    for score in case[1:]:
        upAVG.append(1 if score > AVG else 0)
    print('{:.3f}%'.format(sum(upAVG)/case[0]*100))

#format 함수 사용법 또 까먹지말고 기억하고 있자 (자유자재로 사용할 수 있도록)