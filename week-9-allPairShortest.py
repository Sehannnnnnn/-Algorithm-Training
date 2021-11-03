import sys
def input():
    return sys.stdin.readline().strip()
#입력
N = int(input())
table = [list(map(int, input().split(' '))) for _ in range(N)]


#플로이드 알고리즘
def floyd_algo(N, table):
    for k in range(N):
        for i in range(N):
            if k==i:
                continue
            else:
                for j in range(N):
                    if j==k or i==j:
                        continue
                    else:
                        table[i][j] = min(table[i][k]+table[k][j], table[i][j])

floyd_algo(N,table)

#출력
for i in table:        
    for j in i:    
        print(j, end=' ')
    print()