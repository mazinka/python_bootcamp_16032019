def add_matrices(a,b):
    result =[]
    for i_row in range(len(a)):
        row = []
        for i_col in range(len(a[i_row])):
            element = a[i_row][i_col] + b[i_row][i_col]
            row.append(element)
        result.append(row)
    return result

def add_matrices_v1(a,b):
    for row_a, row_b in zip(a,b):
        row =[]
        for el_a, el_b in zip(row_a,row_b):
            row.append(element)
        result.append(row)
    return result


def sub_matrices(a,b):
    result =[]
    for i_row in range(len(a)):
        row = []
        for i_col in range(len(a[i_row])):
            element = a[i_row][i_col] - b[i_row][i_col]
            row.append(element)
        result.append(row)
    return result
