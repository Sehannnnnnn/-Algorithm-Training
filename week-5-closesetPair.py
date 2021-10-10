import math

#피타고라스 정리
def distanceOf(dot1, dot2):
    distance = math.sqrt((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2)
    return distance

#use QuickSort x좌표로 정렬
def listupXcordiante(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left,right,equal =[],[],[]
    for a in arr:
        if a[0] < pivot[0]:
            left.append(a)
        elif a[0] > pivot[0]:
            right.append(a)
        else:
            equal.append(a)
    return listupXcordiante(left) + equal + listupXcordiante(right)

#리스트 분할
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

#무지성 짝 찾기 n^2
def closestPair_BruteForce(arr):
    distance_list = []
    for i in arr:
        arr.remove(i)
        for j in arr:
            distance_list.append(distanceOf(i,j))   
    return min(distance_list)

#분할정복 알고리즘
def closestPair_Divideconquer(arr):
    if len(arr) <= 3:
        return closestPair_BruteForce(arr)
    temp = arr
    arr = list_chunk(arr, int(len(arr)//2))
    left_zone = arr[0]
    right_zone = arr[1]
    cp_left = closestPair_Divideconquer(left_zone)
    cp_right = closestPair_Divideconquer(right_zone)
    d = min(cp_left,cp_right)
    
    midXCordinate = right_zone[0][0]
    midZone_R, midZone_L  = midXCordinate + d, midXCordinate - d
    midZone = [i for i in temp if i[0] < midZone_R and i[0] > midZone_L]
    if len(midZone) <= 1:
        return d
    else:
        d = min(d, closestPair_BruteForce(midZone))
        return d

#실행
dotsCount = int(input())

space = []

for i in range(dotsCount):
    dot = [int(cordinate) for cordinate in input().split(',')]
    space.append(dot)

space = listupXcordiante(space)
print("{:.6f}".format(closestPair_Divideconquer(space)))


