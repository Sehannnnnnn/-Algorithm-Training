#그리디 1105번 문제 팔

l, r = map(str,input().split())
ans = 0

if len(l) != len(r):
    print(0)
else:
    for i in range(1, len(l)):
        if l[i] != r[i]:
            break
        else:
            if l[i] == '8':
                ans += 1
    print(ans)