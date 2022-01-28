a=1

for i in range(3):
    a *= int(input())

a = str(a)
for i in range(10):
    print(a.count(str(i)))

#count함수는 문자열,list 내의 원소의 개수를 세는데 사용한다.$$