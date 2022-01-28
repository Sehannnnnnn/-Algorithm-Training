import math

x, y = map(int,input().split())
z = (y*100)//x


if z >= 99:
    print(-1)
else:
    print(math.ceil((-100*y+x*z+x)/(100-z-1)))