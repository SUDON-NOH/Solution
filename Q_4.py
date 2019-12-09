def solution(n, m):
    a = n
    b = m
    for i in range(m):
        n, m = m, n % m
        if m == 0:
            break
    answer = [n, a*b//n]
    return answer

