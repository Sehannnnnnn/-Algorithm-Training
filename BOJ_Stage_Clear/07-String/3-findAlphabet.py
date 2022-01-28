from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

text = input()
a = ''
for _ in alphabet_list:
    a += str(text.find(_)) + ' '

print(a)
