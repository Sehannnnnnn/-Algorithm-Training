import sys

a, b = sys.stdin.readline().split()
new_a, new_b = '', ''
for i in range(1,4):
    new_a += a[-i]
    print(new_a)
    new_b += b[-i]
    print(new_b)
new_a, new_b = int(new_a), int(new_b)
print(max([new_a, new_b]))