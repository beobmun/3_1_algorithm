#알고리즘 : 다항식 곱셈을 이중 for 문을 통해 구현

def case_len_one(f, g):
    if (f[0] == 0):
        return ([0])
    elif (f[0] == 1):
        return (g)
    q = list([0] * len(g))    
    for i in range(len(g)):
        q[i] = g[i] * f[0]
    return (q)

def solution(f, g):
    if (len(f) == 1):
        return (case_len_one(f, g))
    elif (len(g) == 1):
        return (case_len_one(g, f))

    q = list([0] * (len(f) + len(g) - 1))
    if (len(f) - f.count(0) > len(g) - g.count(0)):
        f, g = g, f
    for i in range(len(f)):
        if (f[i] == 0): continue
        for j in range(len(g)):
            if (g[j] == 0): continue
            q[i + j] += f[i] * g[j]
    return (q)