def fibo_chicken(num):
    arr = [0,1]
    _curr,_next,_temp = 0,1,0
    index = 0
    answer = 0
    ##num 보다 작은 피보나치 수열 만들기 ARR
    while _temp < num:    
        _temp = _curr + _next
        arr.append(_temp)
        _curr = _next
        _next = _temp
        index += 1
    
    #num이 피보나치 수열일 경우 n-1 값 반환
    if num == arr[index + 1]:
        answer = arr[index]
        return answer

    #num이 피보나치 수열 아닐 경우
    else:
        while True:
            answer += arr[index-1]
            num = num - arr[index]
            #피보나치 수열에서 counter값 찾기
            for i in range(index):
                if arr[i] > num:
                    index = i-1
                    break
            if num == 0: 
                break
        return answer


num = int(input())
print(fibo_chicken(num))