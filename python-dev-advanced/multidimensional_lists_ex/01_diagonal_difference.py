def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

def primary_diagonal_sum(matrix):
    """
    :param matrix: [[row_1][row2_]...[row_n]]
    :return: integer
    """
    n = 0
    sum_diagonal = 0
    for row in matrix:
        sum_diagonal += row[n]
        n += 1
    return sum_diagonal

def secondary_diagonal_sum(matrix):
    """
       :param matrix: [[row_1][row2_]...[row_n]]
       :return: integer
       """
    n = len(matrix)-1
    sum_diagonal = 0
    for row in matrix:
        sum_diagonal += row[n]
        n -= 1
    return sum_diagonal

def diagonal_difference(primary_diagonal, secondary_diagonal):
    return abs(primary_diagonal-secondary_diagonal)

# driver
n = int(input())
matrix = [read_int_list_from_input(' ') for _ in range(n)]
print(diagonal_difference(
    primary_diagonal_sum(matrix),
    secondary_diagonal_sum(matrix)
))