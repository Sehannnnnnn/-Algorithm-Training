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