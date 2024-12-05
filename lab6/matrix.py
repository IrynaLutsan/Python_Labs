def get_column(mtrx, clmn):
    column = []
    for i in range(0, len(mtrx)):
        column.append(mtrx[i][clmn])
    return column

def set_column(mtrx, clmn, vals):
    for i in range(0, len(mtrx)):
        mtrx[i][clmn] = vals[i]
        
def less(a, b):
    if a < b:
        return True
    else:
        return False

def bigger(a, b):
    if a > b:
        return True
    else:
        return False

def bubble_sort(arr, f):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1, i, -1):
            if f(arr[j], arr[j-1]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def mult_transform(m):
    result = []
    first_idx = 0
    for row in m:
        result.append(1)
        for i in range(first_idx, len(row)):
            result[-1] *= row[i]   
        first_idx += 1      
    return result

def arithmetic_mean(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum / len(lst)    

def print_matrix(m):
    for row in m:
        print("|\t", end = "")
        for elem in row:
            print(elem, end = "\t")
        print("|")
        
def main():
    matrix = [[50, 98, -4, 85, -8], 
            [40, 73, -2, -9, -19], 
            [ 1,  6, 73,  21, 0],
            [ 0, 25,  2, -5, -3],
            [99, 19, 95, 92, -7]]

    print("matrix before sorting")
    print_matrix(matrix)

    for i in range(0, len(matrix[0])):
        column = get_column(matrix, i)
        column = bubble_sort(column, less)
        set_column(matrix, i, column)

    print("matrix after sorting")
    print_matrix(matrix)

    transformed_matrix = mult_transform(matrix)
    print("transformed matrix")
    print(transformed_matrix)
    print(f"arithmetic mean = {arithmetic_mean(transformed_matrix)}")
    
if __name__ == "__main__":
    main()