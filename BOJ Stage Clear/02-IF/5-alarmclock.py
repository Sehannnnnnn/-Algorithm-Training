a, b = map(int,input().split())

if b > 45:
    print(a, b-45)
else:
    if a==0:
        if b+60-45 == 60:
            print(a, 0)
        else:
            print(23, b+60-45)
    else:
        if b+60-45 == 60:
            print(a, 0)
        else:
            print(a-1, b+60-45)