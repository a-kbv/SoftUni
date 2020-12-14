from collections import deque

def create_matrix(rows, columns):
    """
    :param rows: integer of how many rows the matrix will have
    :param columns: integer of how many columns(elements) each row will have
    :return: [[row_1][row2_]...[row_n]]
    """
    matrix = []
    for _ in range(rows):
        line = deque(input().split(' '))
        matrix.append([int(line.popleft()) for el in range(columns) if len(line)])
    return matrix

def primary_diagonal_sum(matrix):
    """
    :param matrix: [[row_1][row2_]...[row_n]]
    :return: integer
    """
    n = 0
    sum_diagonal = 0
    for row in matrix:
        sum_diagonal += row[n]
        n+=1
    return sum_diagonal

# driver
rows = columns = int(input())
matrix_1 = create_matrix(rows, columns)
print(primary_diagonal_sum(matrix_1))