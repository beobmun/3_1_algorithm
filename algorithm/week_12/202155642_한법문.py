#알고리즘 : 오른쪽, 왼쪽 사각형 설정 후 null, point, line의 경우를 체크하고 아닌 경우는 겹치는 경우로 리턴

def split_rectangle(coordinate):
    temp_a = {"x_left": coordinate[0], "x_right": coordinate[2], "y_bottom": coordinate[1], "y_top": coordinate[3]}
    temp_b = {"x_left": coordinate[4], "x_right": coordinate[6], "y_bottom": coordinate[5], "y_top": coordinate[7]}
    if (temp_a["x_left"] > temp_b["x_left"]):
        return (temp_b, temp_a)
    return (temp_a, temp_b)

def case_null(left_rec, right_rec):
    if (left_rec["y_top"] < right_rec["y_bottom"]):
        return (True)
    elif (left_rec["y_bottom"] > right_rec["y_top"]):
        return (True)
    elif (left_rec["x_right"] < right_rec["x_left"]):
        return (True)
    return (False)

def case_point(left_rec, right_rec):
    if (left_rec["x_right"] == right_rec["x_left"]):
        if (left_rec["y_top"] == right_rec["y_bottom"] or left_rec["y_bottom"] == right_rec["y_top"]):
            return (True)
    return (False)

def case_line(left_rec, right_rec):
    if (left_rec["y_top"] == right_rec["y_bottom"] or left_rec["y_bottom"] == right_rec["y_top"]):
        if (left_rec["x_left"] <= right_rec["x_right"] < left_rec["x_right"]):
            return (True)
    elif (left_rec["x_right"] == right_rec["x_left"]):
        if (left_rec["y_bottom"] <= right_rec["y_bottom"] < left_rec["y_top"] or \
            left_rec["y_bottom"] <= right_rec["y_top"] < left_rec["y_top"]):
            return (True)
    return (False)

def solution(coordinate):
    left_rec, right_rec = split_rectangle(coordinate)
    if (case_null(left_rec, right_rec)):
        return (0)
    elif (case_point(left_rec, right_rec)):
        return (1)
    elif (case_line(left_rec, right_rec)):
        return (2)
    return (3)