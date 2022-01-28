import sys

a, b = sys.stdin.readline().split()
new_a, new_b = '', ''
for i in range(1,4):
    new_a += a[-i]
    new_b += b[-i]

new_a, new_b = int(new_a), int(new_b)
print(max([new_a, new_b]))