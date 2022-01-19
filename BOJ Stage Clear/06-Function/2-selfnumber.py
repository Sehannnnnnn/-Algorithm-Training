selfnums = set()

for num in range(1,10001):
    for n in str(num):
        num += int(n)
    selfnums.add(num)
    if num in selfnums:
        pass
    else:
        print(num)