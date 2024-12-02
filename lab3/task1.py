def min_elem(lst):
    a = lst[0]
    idx = 0
    for i in range(len(lst)):
        if lst[i] < a:
            a = lst[i]
            idx = i
    return (a, idx)


def sum_of_min2(lst):
    tmp_lst = lst[:]
    min1, idx1 = min_elem(tmp_lst)
    del tmp_lst[idx1]
    min2, idx2 = min_elem(tmp_lst)
    return min1 + min2
    
    
    
lst1 = [x for x in range(10)]
lst2 = [9-x for x in range(10)]
lst3 = [9 for x in range(10)]
lst4 = [78, 55, 90, 43, 21, 98]
print(sum_of_min2(lst1), lst1)
print(sum_of_min2(lst2), lst2)
print(sum_of_min2(lst3), lst3)
print(sum_of_min2(lst4), lst4)