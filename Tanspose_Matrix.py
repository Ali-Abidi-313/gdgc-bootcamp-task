def transpose_matrix(a):
    result = []  
    for j in range(len(a[0])):  
        row = []  
        for i in range(len(a)):  
            row.append(a[i][j])  
        result.append(row)  
    return result  