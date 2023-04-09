#알고리즘: front 모양을 side 길이만큼 확장 후 side 와 top 모양에 없는 건 비우기

def impossible_case(front, side, top):
    if not len(front) or not len(side):
        return (True)
    if (len(top)):
        for t in top:
            if not (type(t) == list) or not (len(t)):
                return (True)
    else:
        return (True)
    if not (max(front) == max(side)):   # 블럭의 높이 수 체크
        return (True)
    elif not (len(front) == len(top)):  # front 폭과 top 가로폭 체크
        return (True)
    max_top = max(max(i) for i in top)
    if not (max_top == len(side)):      # side 폭과 top_max(=위에서 봤을 때 뒤로 제일 많이 나간 곳) 체크
        return (True)
    return (False)

def solution(front, side, top):
    if (impossible_case(front, side, top)):
        return (0)
    stacked_block = []
    for _ in range(0, len(side)):
        stacked_block += [list(front)]

    for i in range(0, len(stacked_block)):
        row = stacked_block[i]
        if (max(row) > side[i]):
            for col in range(0, len(front)):
                if (row[col] > side[i]):
                    row[col] = side[i]

    for col in range(0, len(top)):
        col_min = min(top[col]) - 1
        col_max = max(top[col]) - 1
        for row in range(0, len(stacked_block)):
            if (row < col_min or row > col_max or not row + 1 in top[col]):
                stacked_block[row][col] = 0
    
    answer = 0
    for r_block in stacked_block:
        answer += sum(r_block)
    return (answer)