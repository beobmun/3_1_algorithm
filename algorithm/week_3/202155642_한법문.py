#알고리즘: N이 100ml 단위가 아닌지 체크 후 단위 조정, for 루프에서 i명이 나눠 마실 수 있는지 확인

def solution(N):
    if N == 0 or N % 100: return (0)
    answer = 1
    n = N // 100
    for i in range(2, n):
        remaining_drink = n - (i * (i + 1) // 2)
        if (remaining_drink < 0): break
        if (remaining_drink == 0 or remaining_drink % i == 0):
            answer += 1 
    return (answer)