def get_matrix(rows=int(input())):
    matrix = []
    for row in range(rows):
        matrix.append([int(x) for x in input().split(', ')])
    return matrix

def even_matrix(matrix):
    for el in range(len(matrix)):
        matrix[el] = [el for el in matrix[el] if not el % 2 ==1]
    return matrix

if __name__ == "__main__":
    matrix = get_matrix()
    print(even_matrix(matrix))