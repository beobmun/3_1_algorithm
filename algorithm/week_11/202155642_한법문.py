#알고리즘: radix sort를 활용해서 정렬 후 연속된 점수 차이 최대값 계산

def sorted_check(arr):
    for i in range(1, len(arr)):
        if (arr[i] < arr[i - 1]):
            return (False)
    return (True)

def max_diff(arr):
    diff = 0
    for i in range(1, len(arr)):
        temp = arr[i] - arr[i - 1]
        if (diff < temp):
            diff = temp
    return (diff)

def radix_sort(arr):                                            # 자리수 :k, 입력: n, 진수: r
    quotient = arr                                              
    while (sum(quotient)):                                      # O(k)
        remainder = [i % 10 for i in quotient]                  #   O(n)
        quotient = [i // 10 for i in quotient]                  #   O(n)
        temp = [],[],[]
        r_list = []
        
        if (min(remainder) == max(remainder)):
            continue
        
        for r in range(min(remainder), max(remainder) + 1):     #   O(r)
            if (r in remainder):
                r_list.append(r)
        
        for r in r_list:                                        #   O(r) 
            for n in range(0, len(arr)):                        #       O(n)
                if (r == remainder[n]):
                    temp[0].append(arr[n])
                    temp[1].append(remainder[n])
                    temp[2].append(quotient[n])

        arr = temp[0]
        remainder = temp[1]
        quotient = temp[2]
                                                                # O(krn)
    return (arr)


def solution(rating):
    if (len(rating) < 2):
        return (0)
    if not (sorted_check(rating)):
        if (sorted_check(rating[::-1])):
            rating = rating[::-1]
        else:
            rating = radix_sort(rating)
    return (max_diff(rating))