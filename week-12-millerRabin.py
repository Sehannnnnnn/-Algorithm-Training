n = int(input())

def Miller_Marbin(n):
    tester = [{2,3},{31,73},{2,7,61},{2,3,5,7,11},{2,3,5,7,11,13},{2,3,5,7,11,13,17}]
    if n < 2 or not n & 1:
        return 0
    if n == 2:
        return 1
    def mrtest(b):
        x = pow(b, t, n)
        if x == 1:
            return True
        for i in range(s):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return False
    s = 0
    t = n - 1
    while not t & 1:
        s += 1
        t >>= 1
    # b 선정
    if n < 1373654:
        b = tester[0]
    elif n < 9080191:
        b = tester[1]
    elif n < 4759123141:
        b = tester[2]
    elif n < 2152302898747:
        b = tester[3]
    elif n < 3474749660383:
        b = tester[4]
    elif n < 341550071728321:
        b = tester[5]
    for _b in b:
        if not mrtest(_b):
            return 0
    return 1

print(Miller_Marbin(n))