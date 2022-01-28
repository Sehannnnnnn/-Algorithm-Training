
a = []

for i in range(9):
    a.append(int(input()))

print(max(a))
print(a.index(max(a))+1)

#index 메서드 -> list에서 특정 요소의 위치값을 반환한다. max 함수와 함께 쓰면 $