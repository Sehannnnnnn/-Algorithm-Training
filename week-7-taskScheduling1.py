import sys

task_num = int(input())
taskList = []

for i in range(task_num):
    taskList.append(list(map(int, sys.stdin.readline().split())))


def quickSort_Ascending(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left,right,equal =[],[],[]
    for a in arr:
        if a[0] > pivot[0]:
            right.append(a)
        elif a[0] < pivot[0]:
            left.append(a)
        else:
            equal.append(a)
    return quickSort_Ascending(left) + equal + quickSort_Ascending(right)

taskList = quickSort_Ascending(taskList)


#task 나누기
def task_by_machine(tasks):
    arr = []
    for task in tasks:
        if not arr:
            arr.append(task)
        else:
            temp = []
            for i in range(len(arr)):
                if arr[i][-1] < task[0]:
                    temp.append(i)
                    break
                else:
                    pass
            if not temp:
                arr.append(task)
            else: 
                arr[min(temp)] = arr[min(temp)] + task

    print(arr)
    return len(arr)

print(task_by_machine(taskList))


