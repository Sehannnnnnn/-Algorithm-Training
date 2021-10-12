monster_hp = int(input())
weapon_count = int(input())


weapon_array = []

# 무기정보 2차원 배열에 삽입
for i in range(weapon_count):
    weapon_attak, weapon_durablity = map(int, input().split())
    weapon_array.append([weapon_attak,weapon_durablity])

# 무기 공격력에 따른 배열 정렬
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left,right,equal =[],[],[]
    for a in arr:
        if a[0] > pivot[0]:
            left.append(a)
        elif a[0] < pivot[0]:
            right.append(a)
        else:
            equal.append(a)
    return quickSort(left) + equal + quickSort(right)

weapon_array = quickSort(weapon_array)


# 
attack_count, weapon_number = 0, 0

while monster_hp > 0:
    if weapon_array[weapon_number][1] == 0:
        weapon_number += 1
    else:
        monster_hp = monster_hp - weapon_array[weapon_number][0]
        weapon_array[weapon_number][1] -= 1
        attack_count += 1

print(attack_count)