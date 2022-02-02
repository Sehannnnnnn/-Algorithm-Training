#그리디 1105번 문제 팔

l, r = input().split()
ans = 0

if len(l) != len(r):
    print(ans)
else:
    for i in range(len(l)):
        if l[i] != r[i]:
            break
        else:
            if l[i] == '8':
                ans += 1
    print(ans)