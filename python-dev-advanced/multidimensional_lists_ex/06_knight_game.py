def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

def read_str_list_from_input(separator=' '):
    return [x for x in input().split(separator)]

if __name__ == "__main__":
    (rows, cols) = read_int_list_from_input(' ')
    matrix = [read_str_list_from_input(' ') for _ in range(rows)]
