T = int(input())
count = 0

for _ in range(T):
    text = input()
    a = []
    tf = True
    for t in text:
        if t in a:
            if a[-1] == t:
                pass
            else:
                tf = False
        else:
            a.append(t) 
    if tf == True:
        count += 1

print(count)