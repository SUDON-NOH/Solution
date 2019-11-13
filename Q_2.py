# 정수 제곱근 판별

def solution(n):
    if float(n**0.5).is_integer() :
        answer = ((n**0.5) + 1)**2

    else:
        answer = -1
    return answer


print(type(10**0.5))


# ==============================================================================

def solution(n):

    x = n ** 0.5

    if x % 1 == 0:
        return (x + 1)**2
    
    return -1