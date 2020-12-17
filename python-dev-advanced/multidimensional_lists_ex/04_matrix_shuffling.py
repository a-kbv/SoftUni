def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

def read_str_list_from_input(separator=' '):
    return [x for x in input().split(separator)]


def check_input(data, rows, cols):
    try:
        (command, row1, col1, row2, col2) = data.split(' ')
    except:
        print("Invalid input!")
        return False, None
    else:
        rows = int(rows)
        cols = int(cols)
        row1 = int(row1)
        col1 = int(col1)
        row2 = int(row2)
        col2 = int(col2)

        if command == 'swap' and \
            row1 < rows and \
            row2 < rows and \
            col1 < cols and\
            col2 < cols:
            return True, command, int(row1), int(col1), int(row2), int(col2)
        else:
            print("Invalid input!")
            return False, None


def swap(matrix, tuple):
    row1, col1, row2, col2 = tuple[2:]

    matrix[row1][col1],\
    matrix[row2][col2] =\
        matrix[row2][col2],\
        matrix[row1][col1]
    return matrix

# DRIVER CODE
if __name__ == "__main__":
    (rows, cols) = read_int_list_from_input(' ')
    matrix = [read_str_list_from_input(' ') for _ in range(rows)]

    data = input()
    while not data == 'END':
        result_data = check_input(data, rows, cols)
        if result_data[0]:
            matrix = swap(matrix, result_data)

            for el in matrix:
                print(' '.join(el))
        data = input()
