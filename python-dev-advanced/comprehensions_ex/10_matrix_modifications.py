def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

def add(matrix, row, col, value):
    matrix[row][col] += value
    return matrix

def subtract(matrix, row, col, value):
    matrix[row][col] -= value
    return matrix

def valid_cordinate(matrix, row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

if __name__ == "__main__":
    n = int(input())
    matrix = [read_int_list_from_input() for _ in range(n)]

    while True:
        data = input().split()
        if data[0] == "END":
            break
        do, row, col, val = data[0], int(data[1]), int(data[2]), int(data[3])

        if do == "Add" and valid_cordinate(matrix, row, col, n):
            matrix = add(matrix, row, col, val)
        elif do == "Subtract" and valid_cordinate(matrix, row, col, n):
            matrix = subtract(matrix, row, col, val)
        else:
            print("Invalid coordinates")

    [print(" ".join(map(str, row)))for row in matrix]

