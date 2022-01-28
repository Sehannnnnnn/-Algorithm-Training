nums = []
for i in range(10):
    nums.append(int(input())%42)

nums = set(nums)
print(len(nums))

#set 함수 -> list요소를 set으로 바꾸어 중복을 제거하는데 사용된다.