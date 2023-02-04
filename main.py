from EROS import *
from time import sleep

def make_all_zero (mat, col_lst, column_no):
    for i in range (column_no, len(mat)):
        for j in range (len(mat)):
            col_lst[j] = mat[j][column_no-1]
        addition(mat, i+1, column_no, -1*(col_lst[i]))

    return mat



def make_all_zero1 (mat, col_lst, column_no):
    for i in range (len(mat)):
        for j in range (len(mat)):
            col_lst[j] = mat[j][column_no-1]
        if i == column_no-1:
            pass
        else:
            # print (-1*(col_lst[i]))
            addition(mat, i+1, column_no, -1*(col_lst[i]))

    return mat



def find_most_zeros (mat):
    num_r = 0
    num_c = 0
    number_r = 0
    number_c = 0
    for i in range (len(mat)):
        a = mat[i].count(0)
        if a > num_r:
            num_r = a
            number_r = i
    
    col = [0 for i in range (len(mat))]
    for i in range (len(mat)):
        for j in range (len(mat)):
            col[i] = mat[j][i]

        a = col.count(0)
        if a > num_c:
            num_c = a
            number_c = j
    
    if num_r >= num_c:
        return number_r, True
    else:
        return number_c, False



def det_of_2 (mat):
    if len(mat) != 2:
        print ("The matrix is not 2x2")
        return None
    else:
        res = (mat[1][1]*mat[2][2]) - (mat[1][2]*mat[2][1])

    return res



def det_of_n (mat):
    if len(mat) == 2:
        return (det_of_2(mat))
    else:
        # for i in range ()
        pass





def Gauss_sol (mat):
    col1 = [0 for i in range (len(mat))]

    for j in range (len(col1)-1):

        for i in range (len(mat)):
            col1[i] = mat[i][j]

        if 1 in col1 and col1.index(1) >= j:
            swap(mat, j+1, col1.index(1)+1)
        else:
            multiple(mat, j+1, (1/col1[j]))

        mat = make_all_zero(mat, col1, j+1)
    
    for i in range (len(mat)):
        col1[i] = mat[i][len(mat)-1]
    
    multiple(mat, len(mat), (1/col1[len(mat)-1]))

    print ()

    return mat


def inverse (mat):
    for i in range (len(mat)):
        for j in range (len(mat)):
            if i == j: 
                mat[i] += [1]
            else:
                mat[i] += [0]
    
    print_mat(mat)

    col1 = [0 for i in range (len(mat))]

    for j in range (len(col1)):

        for i in range (len(mat)):
            col1[i] = mat[i][j]

        if 1 in col1 and col1.index(1) >= j:
            swap(mat, j+1, col1.index(1)+1)
        else:
            multiple(mat, j+1, (1/col1[j]))

        mat = make_all_zero1(mat, col1, j+1)

    for i in range (len(mat)):
        mat[i] = mat[i][len(mat):]

    return mat



def matrix_multiplication (a, b):
  print (a, '\n', b)  
  col1 , col2 = len(a), len(b)
  c, d = a[0], b[0]
  row1, row2 = len(c), len(d)
  
  if col2 == row1:
    p = []
    for i in range (col1):
      q = []
      for j in range (row2):
        sm = 0
        for k in range (col2):  
          g = a[i][k] * b[k][j]
          sm += g
        q.append (round(sm, 2))
          
      p.append (q)
        
    return p
  else:
    return ('The number of columns in Matrix A does not equal the number of rows in Matrix B required for Matrix Multiplication.')




# n = int(input('Enter the number of variables: '))
# mat = []
# for i in range (n):
#     mat.append([])
#     for j in range (n):
#         a = input (f'Equation {i+1}, x{j+1} = ')
#         mat[i].append(int(a))
#     b = input (f"b{i+1} = ")
#     mat[i].append (int(b))

# mat = [[2,5,2],[3,-2,4],[-6,1,-7]]
# while True:
#     if len(mat) != len(mat[0]):
#         print ('The number of rows and columns does not match')
#     else:
#         break
# aug_mat = [[2,5,2,-38],[3,-2,4,17],[-6,1,-7,-12]]

# print ()
# print_mat(mat)
# sleep(1)
# print ()


# mat1 = [[1,2,3],[8,9,5],[2,0,5]]
# mat = mat1.copy()
# mat = [[1,2,3],[8,9,5],[2,0,5]]

# print_mat(mat)

# res = (inverse(mat1))
# print ("yay hai inverse")
# print_mat(res)
# print ("ye hai dono ko multiply")
# print_mat (matrix_multiplication(mat, res))
# print_mat (inverse(mat1))

# res = Gauss_sol(mat)
# print_mat(res)

# sol = []

# for i in res:
#     sol.append(i[-1])
#     i.pop(i.index(i[-1]))

# print ()
# print (sol)
# print_mat(res)

# for i in reversed (range (len(mat))):
#     pass
def main ():
    while True:
        a = int(input ("What do you want to do:\n1. solving an nxn equation\n2. inverse of a matrix\n3. multiply 2 matrices\n"))
        try:
            if a == 1 or a == 2:
                break
        except:
            print("Please select a valid number")
    if a == 1:
        n = int(input('Enter the number of variables: '))
        mat = []
        for i in range (n):
            mat.append([])
            for j in range (n):
                a = input (f'Equation {i+1}, x{j+1} = ')
                mat[i].append(int(a))
            b = input (f"b{i+1} = ")
            mat[i].append (int(b))
        res = Gauss_sol(mat)
        print_mat(res)
    elif a == 2:
        n = int(input('Enter the number of rows: '))
        mat = []
        mat1 = []
        for i in range (n):
            mat.append([])
            mat1.append([])
            for j in range (n):
                a = int(input(f'Enter the element {i+1}{j+1}: '))
                mat[i].append(a)
                mat1[i].append(a)
        res = inverse(mat)
        print(f'\nThe inverse of the matrix\n{print_mat(mat1)}\nis\n{print_mat(res)}')


main()
# import random
# lst = ['kal', 'tue']
# print (random.choice(lst))