from collections import deque

def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

def snake_path(rows, cols, snake):
    matrix = [[] for row in range(rows)]
    temp_snake = deque(snake * 100)

    for row in range(rows):
        for col in range(cols):
            if row % 2 == 0:
                matrix[row].append(temp_snake.popleft())
            else:
                matrix[row].insert(0, temp_snake.popleft())
    return matrix

def repr_path(matrix):
    for el in matrix:
        print(''.join(el))

if __name__ == "__main__":
    (rows, cols) = read_int_list_from_input(' ')
    snake = input()
    matrix = snake_path(rows, cols, snake)
    repr_path(matrix)

