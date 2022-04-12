def quadrillage():
    lst = []
    a = 0
    while a < 1170:
        a += 30
        lst.append(((a, 0), (a, 1200)))
    lst2 = []

    a = 0
    while a < 1170:
        a += 30
        lst2.append(((0, a), (1200, a)))
    return (lst + lst2)