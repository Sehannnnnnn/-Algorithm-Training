orignN = int(input())
t = 0
n = orignN

while (True):
    t = t+1
    a = n//10
    b = n%10
    new_a = b
    new_b = (a+b)%10
    n = new_a*10+new_b
    if n == orignN:
        print(t)
        break
