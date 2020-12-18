
def read_str_list_from_input(separator=' '):
    return [x for x in input()]

def is_valid(pos, size):
    row = pos[0]
    col = pos[1]
    return 0 <= row < size and 0 <= col < size

def get_killed_knights(board, row, col, size):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_pos = [row + rows[i], col + cols[i]]
        if is_valid(current_pos, size) and\
            board[current_pos[0]][current_pos[1]] == "K":
            killed_knights += 1

    return killed_knights

def chess_board(board, n):

    total_kills = 0
    while True:
        most_kills = 0
        to_kill = []

        for row in range(n):
            for col in range(n):
                if board[row][col] == "K":
                    killed_knights = get_killed_knights(board, row, col, n)
                    if killed_knights > most_kills:
                        most_kills = killed_knights
                        to_kill = [row, col]

        if most_kills == 0:
            break

        to_kill_row = to_kill[0]
        to_kill_col = to_kill[1]
        board[to_kill_row][to_kill_col] = "0"
        total_kills += 1

    print(total_kills)
    # for row in board:
    #     print(row)


if __name__ == "__main__":
    n = int(input())
    board = [read_str_list_from_input(' ') for _ in range(n)]
    chess_board(board, n)

