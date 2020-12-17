def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

def read_list_from_input(separator=' '):
    return [(x) for x in input().split(separator)]

def is_all_char_sane(string):
    char = string[1]
    is_valid = True
    for ch in string:
        if ch != char:
            is_valid = False
            break
        else:
            continue
    return is_valid


def matching(matrix, rows, cols):
    cnt_match =0
    for row in range(rows - 1):
        for col in range(cols - 1):
        # starting from the element in top-left take 2x2 matrix
            submatrix = []
            current_chars = ''
            row_cnt = 0
            for r in range(row, row + 2):
                submatrix.append([])
                for c in range(col, col + 2):
                    submatrix[row_cnt].append(matrix[r][c])
                    current_chars += matrix[r][c]
                row_cnt += 1
            if is_all_char_sane(current_chars):
                cnt_match += 1
    if cnt_match > 1:
        return cnt_match
    else:
        return 0

if __name__ == "__main__":
    (rows, cols) = read_int_list_from_input(' ')
    matrix = [read_list_from_input(' ') for _ in range(rows)]
    print(matching(matrix, rows, cols))

