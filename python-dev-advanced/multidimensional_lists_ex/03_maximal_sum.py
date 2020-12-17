def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

def get_square(matrix, rows, cols):
    best_sum = -999999999
    best_matrix = []

    for row in range(rows - 2):
        for col in range(cols - 2):
            # starting from the element in top-left take 3x3 matrix
            submatrix = []
            current_sum = 0
            row_cnt = 0
            for r in range(row, row + 3):
                submatrix.append([])
                for c in range(col, col + 3):
                    submatrix[row_cnt].append(matrix[r][c])
                    current_sum += matrix[r][c]
                row_cnt += 1
            if current_sum > best_sum:
                best_sum = current_sum
                best_matrix = submatrix


    return best_matrix, best_sum

def print_best(best_matrix, best_sum):
    print(f"Sum = {best_sum}")
    for row in best_matrix:
        print(' '.join(str(el) for el in row))

# Driver code
if __name__ == "__main__":
    (rows, columns) = read_int_list_from_input(' ')
    matrix = [read_int_list_from_input(' ') for _ in range(rows)]
    best_matrix, best_sum = get_square(matrix, rows, columns)
    print_best(best_matrix, best_sum)
