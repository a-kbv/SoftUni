from collections import deque

def create_matrix(row):
    """
    :param rows: integer of how many rows the matrix will have
    :return: [[row_1][row2_]...[row_n]]
    """
    matrix = []
    for _ in range(row):
        matrix.append([input()])
    return matrix

def search_for_symbol(matrix):
    sym = input()
    """
    :param matrix: [[row_1][row2_]...[row_n]]
    :param sym char
    :return: integer
    """
    ro_w = -1
    co_l = -1
    for row in matrix:
        ro_w += 1
        for el in row[0]:
            co_l += 1
            if el == sym:
                return (ro_w,co_l)
        co_l = -1
    return (f'{sym} does not occur in the matrix')

# driver
rows = int(input())
matrix_1 = create_matrix(rows)
print(search_for_symbol(matrix_1))
