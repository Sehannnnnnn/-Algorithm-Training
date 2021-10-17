# 오름차순 정렬 함수
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

#실행
node, edge = map(int, input().split())

edge_set = []
for i in range(edge):
    edge_set.append(list(map(int, input().split())))

#edge 정렬
edge_set = quickSort_Ascending(edge_set)


#find & union 알고리즘
arr = [i for i in range(node+1)]
def find(x):
    if arr[x] != x:
        return find(arr[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        arr[b] = a
    else: 
        arr[a] = b


#크루스컬 MST 알고리즘
def kruskal_MST(Edge_set, n):
    totalMST = 0
    edgeCount = 0
    for element in Edge_set:
        if edgeCount == n-1:
            break
        nodeA, nodeB  = element[0],element[1]
        edgelength = element[2]
        if find(nodeA) != find(nodeB):
            union(nodeA, nodeB)
            totalMST += edgelength
            edgeCount += 1
    return totalMST



print(kruskal_MST(edge_set, node))