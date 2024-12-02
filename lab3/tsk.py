def sum_of_min2(lst):
    a, b, *_= lst
    print(a, b, _)
    if lst[0] < lst[1]:
        a, b, *_ = lst
    else:
        b, a, *_ = lst 
        
    for i in range(2, len(lst)):
        if lst[i] < a:
            b, a = a, lst[i]
        elif lst[i] < b:
            b = lst[i]
            
    return a + b

    
lst1 = [x+1 for x in range(10)]
lst2 = [10-x for x in range(10)]
lst3 = [9 for _ in range(10)]
lst4 = [78, 55, 90, 43, 21, 98, 21]
print(sum_of_min2(lst1), lst1)
print(sum_of_min2(lst2), lst2)
print(sum_of_min2(lst3), lst3)
print(sum_of_min2(lst4), lst4)