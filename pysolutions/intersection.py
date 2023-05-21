def op_intersection(n1, n2):
    n1 = set(list1)
    n2 = set(list2)
    res = n1.intersection(n2)
    return res


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 3, 6, 232, 8, 3445, 353443, 43]
print(op_intersection(list1, list2))
