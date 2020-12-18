def get_matrix(rows=int(input())):
    matrix = []
    for row in range(rows):
        matrix.append([int(x) for x in input().split(', ')])
    return matrix

def flatten_matrix(matrix):
    return [y for x in matrix for y in x]
# [ y for x in non_flat if len(x) > 2 for y in x ]

if __name__ == "__main__":
    matrix = get_matrix()
    print(flatten_matrix(matrix))