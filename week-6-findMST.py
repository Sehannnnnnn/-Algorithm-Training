# 내림차순 정렬 함수
def quickSort_Ascending(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left,right,equal =[],[],[]
    for a in arr:
        if a[2] > pivot[2]:
            right.append(a)
        elif a[2] < pivot[2]:
            left.append(a)
        else:
            equal.append(a)
    return quickSort_Ascending(left) + equal + quickSort_Ascending(right)


def kruskal_MST(Edge_set, n):
    quickSort_Ascending(Edge_set)
    # 최소 가중치 +

    # 순환하는 지 체크하고 버릴지 결정
    return


#실행
node, edge = map(int, input().split())

edge_set = []
for i in range(edge):
    edge_set.append(list(map(int, input().split())))

print(edge_set)

edge_set = quickSort_Ascending(edge_set)
print(edge_set)