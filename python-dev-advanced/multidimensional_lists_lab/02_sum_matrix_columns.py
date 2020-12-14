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

def sum_matrix_rows(matrix):
    """
    :param matrix [[row_1][row2_]...[row_n]]
    :returns list with sum of all rows of matrix
    """
    return [sum(el) for el in matrix]

def sum_matrix_col(matrix):
    """
    :param matrix: [[row_1][row2_]...[row_n]]
    :return: list with sum of all columns in matrix
    """
    answer = []
    for column in range(len(matrix[0])):
        t = 0
        for row in matrix:
            t += row[column]
        answer.append(t)
    return answer

def sum_matrix_total(matrix):
    """
    :param matrix: [[row_1][row2_]...[row_n]]
    :return: integer with sum of all rows and columns in matrix
    """
    return [sum([sum(el) for el in matrix])][0]

# driver code
row, columns = [int(el) for el in input().split(', ')]

matrix_1 = create_matrix(row,columns)
sum_col = sum_matrix_col(matrix_1)
print('\n'.join(map(str, sum_col)))