#알고리즘: 첫번쨰 for 문 - 뒷사람과의 등급비교, 두번째 for 문 - 앞사람과의 등급비교

def solution(rating):
    len_rating = len(rating)
    if not (len_rating): return (0)
    elif (len_rating == 1): return (1)
    candy_list = [1] * len_rating
    if (rating[0] > rating[1]):
        candy_list[0] += 1
    for i in range(1, len_rating - 1):
        if (rating[i] > rating[i - 1]):
            candy_list[i] = candy_list[i - 1] + 1
    if (rating[-1] > rating[-2]):
        candy_list[-1] = candy_list[-2] + 1
    for j in range(len_rating - 2, 0, -1):
        if (rating[j] > rating[j + 1] and candy_list[j] < candy_list[j + 1] + 1):
            candy_list[j] = candy_list[j + 1] + 1
    return (sum(candy_list))