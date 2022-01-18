a = int(input())
b = input()

for i in range(len(b)):
    j = len(b)-i-1
    print(a*int(b[j]))

print(a*int(b))



