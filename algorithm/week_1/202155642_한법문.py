#알고리즘 : 입력받은 문자열을 "0"을 기준으로 split 한 뒤 이중for 문을 이용하여 연속적인 확진자수 덧셈하여 비교

def solution(confirmed_case):
    answer = 0
    splited_case = confirmed_case.split("0")
    
    for continuous in splited_case:
        sum_daily = 0
        for daily in continuous:
            if ('0' <= daily and '9' >= daily):
                sum_daily += ord(daily) - ord('0')
            elif ('a' <= daily and 'z' >= daily):
                sum_daily += ord(daily) - ord('a') + 10
        if (sum_daily > answer):
            answer = sum_daily
            
    return answer