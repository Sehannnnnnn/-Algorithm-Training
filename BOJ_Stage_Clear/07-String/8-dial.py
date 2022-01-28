dial = {
    2: ['A','B','C'],
    3: ['D','E','F'],
    4: ['G','H','I'],
    5: ['J','K','L'],
    6: ['M','N','O'],
    7: ['P','Q','R','S'],
    8: ['T','U','V'],
    9: ['W','X','Y','Z'],
}

text = input()

i = 0
time = 0
while (len(text) != i):
    for key, value in dial.items():
        if text[i] in value:
            time += key
    i += 1

print(time+len(text))