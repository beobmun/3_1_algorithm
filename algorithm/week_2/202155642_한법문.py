#알고리즘 : 문자열에서 요구조건에 맞게 숫자 설정, 소수 인지 판단 후 소수일 경우 몇번 쨰 소수인지 카운트

def prime_check(num):
    if (num == 2):
        return (True)
    elif (num < 2 or num % 2 == 0):
        return (False)
    sq_num = int(num ** (1/2)) + 1
    for i in range(2, sq_num):
        if (num % i == 0):
            return (False)
    return (True)

def solution(car_number):
    chk_num = int((((int(car_number[:3]) + int(car_number[-4:-1]))) / int(car_number[-1:])) + 0.5)
    if not prime_check(chk_num):
        return (0)
    answer = 1
    for i in range(2, chk_num):
        if (prime_check(i)):
            answer += 1
    return (answer)