# 제일 작은 수 제거하기

def solutin(arr):

    if len(arr) == 1 or len(arr) == 0:
        answer = [-1]
    else:
        arr.remove(min(arr))
        answer = arr

    return answer