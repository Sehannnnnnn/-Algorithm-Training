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
print(taskList)

arr = []
#TaskTime
def task_by_machine(tasks):
    if len(tasks) == 0:
        return len(arr)
    a = tasks[0]
    arr.append(a)
    tasks.remove(a)
    restTask = []
    for task in tasks:
        if arr[-1][-1] < task[0]:
            arr[-1] += task
        else: 
            restTask.append(task)

    task_by_machine(restTask)
    
    

print(task_by_machine(taskList))

#pop메소드 사용 최소화