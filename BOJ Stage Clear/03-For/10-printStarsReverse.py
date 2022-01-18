# n = int(input())
# a = ''
# for i in range(n):
#     a += ' '

# for i in range(n):
#     a += '*'
#     a = a[1:]
#     print(a)

#우수정답

a = int(input())

for i in range(1,a+1):
    print(" "*(a-i)+"*"*i)