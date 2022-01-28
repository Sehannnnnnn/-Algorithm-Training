text = input().upper()

a = {}
s = set(text)
for t in s:
    a[t] = text.count(t)

result = [k for k,v in a.items() if max(a.values()) == v]

if len(result) > 1:
    print('?')
else: 
    print(result[0])
