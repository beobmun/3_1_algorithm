#알고리즘 : penalty를 적용하여 Edit Distance를 활용

def setting_table(src, dest):
    table = list()
    for _ in range(len(src) + 1):
        table.append(list([0] * (len(dest) + 1)))
    for col in range(1, len(dest) + 1):
        table[0][col] = col
    for row in range(1, len(src) + 1):
        table[row][0] = row
    return (table)

def solution(src, dest, pen_1, pen_2):
    table = setting_table(src, dest)

    for row in range(1, len(src) + 1):
        src_c = src[row - 1]
        for col in range(1, len(dest) + 1):
            dest_c = dest[col - 1]
            if (src_c == dest_c):
                table[row][col] = table[row - 1][col - 1]
            else:
                optimal = min(table[row][col - 1] + pen_1, table[row - 1][col] + pen_1, table[row - 1][col - 1] + pen_2)
                table[row][col] = optimal

    return (table[len(src)][len(dest)])