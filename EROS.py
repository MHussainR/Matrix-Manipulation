def print_mat (mat):
    for i in range (len(mat)):
        print (mat[i])



def addition (mat, main_row, other_row, scalar_multiple=1):
    row1 = mat[main_row-1]
    row2 = mat[other_row-1]
    row3 = [0 for j in range (len(row1))]
    for i in range (len(row1)):
        val = row1[i] + row2[i]*scalar_multiple
        row3[i] = round(val,10)

    mat[main_row-1] = row3

    if scalar_multiple < 0:
        op = '-'
    else:
        op = '+'

    print (f'R{main_row} => R{main_row} {op} {abs(scalar_multiple)}R{other_row}')
    print_mat(mat)

    return mat



def swap (mat, main_row, other_row):
    mat[main_row-1], mat[other_row-1] = mat[other_row-1], mat[main_row-1]

    print (f'R{main_row} <==> R{other_row}')
    print_mat(mat)

    return mat



def multiple (mat, main_row, multiple):
    row1 = mat[main_row-1]
    row2 = [0 for i in range (len(row1))]

    for i in range (len(row1)):
        row2[i] = row1[i]*multiple

    mat[main_row-1] = row2

    print (f'R{main_row} ==> {multiple}R{main_row}')
    print_mat(mat)

    return mat