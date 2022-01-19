N = int(input())

def HanSu(N):
    if N <= 100:
        return N
    else:
        count = 99
        for num in range(101, N+1):
            a = set()
            for i in range(len(str(num))-1):
                a.add(int(str(num)[i+1])-int(str(num)[i]))
            if len(a) == 1:
                count += 1
            else:
                pass
        return count

print(HanSu(N))