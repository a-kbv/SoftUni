

def read_matrix(size):
    matrix = [[] * size for _ in range(size)]
    for row in range(size):
        line = input()
        for col in range(size):
            matrix[row].append(line[col])
    return matrix

def snake_position(matrix):
    snake_row = ""
    snake_col = ""
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "S":
                snake_row = row
                snake_col = col
                return snake_row, snake_col
    return snake_row, snake_col

def burrow_pos(matrix):
    burrows = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "B":
                burrows.append((row, col))
    return burrows

def is_food(matrix, row, col):
    if matrix[row][col] == "*":
        return True
    return False

def is_not_dead(matrix, row, col):
    if row in range(len(matrix)):
        if col in range(len(matrix)):
            return True
    return False

def is_burrow(matrix, row, col):
    if matrix[row][col] == "B":
        return True
    return False


def move(matrix, direction, food, is_alive):

    if direction == "left":
        row, col = snake_position(matrix)
        if is_not_dead(matrix, row, col - 1):
            if is_food(matrix, row, col - 1):
                food += 1
            matrix[row][col] = "."
            matrix[row][col - 1] = "S"
        else:
            matrix[row][col] = "."
            is_alive = False
        return matrix, food, is_alive

    elif direction == "right":
        row, col = snake_position(matrix)
        if is_not_dead(matrix, row, col + 1):
            if is_food(matrix, row, col + 1):
                food += 1
            matrix[row][col] = "."
            matrix[row][col + 1] = "S"
        else:
            matrix[row][col] = "."
            is_alive = False
        return matrix, food, is_alive

    elif direction == "down":
        row, col = snake_position(matrix)
        if is_not_dead(matrix, row + 1, col):
            if is_food(matrix, row + 1, col):
                food += 1
            matrix[row][col] = "."
            matrix[row + 1][col] = "S"
        else:
            matrix[row][col] = "."
            is_alive = False
        return matrix, food, is_alive

    elif direction == "up":
        row, col = snake_position(matrix)
        if not is_not_dead(matrix, row - 1, col):
            if is_food(matrix, row - 1, col):
                food += 1
            matrix[row][col] = "."
            matrix[row - 1][col] = "S"
        else:
            matrix[row][col] = "."
            is_alive = False
        return matrix, food, is_alive

    return matrix, food, is_alive

if __name__ == "__main__":
    size = int(input())
    food = 0
    matrix = read_matrix(size)
    is_alive = True

    while True:
        if food >= 10:
            print("You won! You fed the snake.")
            break
        if not is_alive:
            print("Game over!")
            break
        direction = input()
        matrix, food, is_alive = move(matrix, direction, food, is_alive)

    print(f"Food eaten: {food}")

    for element in matrix:
        for char in element:
            print(char, end="")
        print()