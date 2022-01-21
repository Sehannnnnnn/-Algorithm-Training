

T = int(input())

for i in range(T):
    num, text = input().split(' ')
    num = int(num)
    result = ''
    for t in text:
        result += t*num
    print(result)