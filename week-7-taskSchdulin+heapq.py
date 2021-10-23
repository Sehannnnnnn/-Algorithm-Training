#heapq 자료구조 사용 (Java의 우선순위 큐와 매우 유사)
import heapq
import sys
def input():
    return sys.stdin.readline().strip()

N = int(input())
array = [list(map(int, input().split(' '))) for _ in range(N)]

array.sort()
answer = 0

pQ = [(array[0][1], array[0][0])]
for i in range(1, len(array)):
    init, end = array[i]

    if pQ[0][0] > init:
        heapq.heappush(pQ, (end, init))
    else:
        while pQ:
            if pQ[0][0] <= init:
                heapq.heappop(pQ)
            else:
                break
        heapq.heappush(pQ, (end, init))

    answer = max(answer, len(pQ))


print(answer)