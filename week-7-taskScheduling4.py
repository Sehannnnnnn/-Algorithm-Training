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
machineList = []
print(taskList)


def find_machine(t,machineList):
    temp = []
    for i in range(len(machineList)):
        if machineList[i][-1] < t[0]:
            temp.append(machineList[i][-1])
        else: pass
    if len(temp) == 0:
        return False
    else: return temp.index(min(temp))+1


print(len(taskList))
while (len(taskList) != 0):
    t = taskList[0]
    print(t)
    a = find_machine(t,machineList)
    print(machineList)
    print(a-1)
    if a == False:
        machineList.append(t)
        print('기계없음', machineList)
    else:
        machineList[a-1] += t
        print('기계찾음', machineList)
    taskList.remove(t)
    print('배정이후:',machineList)
    print('잔여taskList', taskList)
    print('')

print(len(machineList))




#pop메소드 사용 최소화
