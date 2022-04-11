lst = []


a = 0
while a < 570:

    a += 30
    lst.append(((a, 0), (a, 600)))
print(lst)
lst2 = []


a = 0
while a < 570:

    a += 30
    lst2.append(((0, a),(600, a)))
print(lst2)
lst3 = (lst + lst2)