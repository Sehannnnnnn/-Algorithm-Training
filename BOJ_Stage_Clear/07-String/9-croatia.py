croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
from string import ascii_lowercase

text = input()

result = 0
for c in croatia:
    result += text.count(c)
    text = text.replace(c, ' ')

for alphabet in ascii_lowercase:
    result+= text.count(alphabet)

print(result)
