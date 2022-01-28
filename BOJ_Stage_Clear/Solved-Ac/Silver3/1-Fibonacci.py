T = int(input())

for i in range(T):
    n = int(input())
    zero = [1,0]
    one = [0,1]
    for j in range(n+1):
        if j > 1:
            zero.append(zero[j-1]+zero[j-2])
            one.append(one[j-1]+one[j-2])
    print(zero[n], one[n])
            

