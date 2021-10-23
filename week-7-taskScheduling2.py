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

arr = []
#TaskTime
def task_by_machine(tasks):
    if len(tasks) == 0:
        return arr
    arr.append(tasks.pop(0))
    i = 0
    while (True):
        try:
            tasks[i]
        except IndexError:
            break
        if arr[-1][-1] < tasks[i][0]:
            print(i)
            arr[-1] += tasks.pop(i)
            print(arr)
        else: 
            i += 1
    task_by_machine(tasks)
    

task_by_machine(taskList)

#배열 쓰지말고 