import sys

T = int(input())

for i in range(T):
    case = sys.stdin.readline()
    score = 0
    countOs = 0
    for OX in case:
        if OX == "O":
            countOs += 1
        else:
            #연속되는 O개수를 세다 X가 나오면 점수를 부여하는 방식
            score += (countOs*(countOs+1))/2
            countOs = 0
            pass
    print(int(score))


#우수답안 출처 - 영지공지
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)