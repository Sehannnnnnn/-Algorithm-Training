#1052번 그리디 알고리즘 실버1

n, k = map(int,input().split())

i = 1
result = 0
while (n > 2**k):
    if n % 2 == 0:
        n = n//2
        i = i * 2
    else:
        n = n + 1
        n = n//2
        result += i
        i = i * 2
    
print(result)

#2진수 bin함수 활용 -> 2진수 변환시 1의 개수 count

n,k = map(int, input().split())

cnt = 0
while bin(n).count('1') > k:
    n += 1
    cnt += 1
print(cnt)