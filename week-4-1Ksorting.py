#입력 받기
case_num = int(input())
array = []

for i in range(case_num):
    a = int(input())
    array.append(a)

#퀵소트 구현
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left,right,equal =[],[],[]
    for a in arr:
        if a > pivot:
            left.append(a)
        elif a < pivot:
            right.append(a)
        else:
            equal.append(a)
    return quickSort(right) + equal + quickSort(left)

sorted = quickSort(array)

#출력
for i in sorted:
    print(i)