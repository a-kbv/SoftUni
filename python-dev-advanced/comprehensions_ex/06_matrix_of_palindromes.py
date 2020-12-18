
def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


# a = 97
# b = 98
# c = 99
def palindromic_matrix(r,c):
    matrix = [[]*r for _ in range(r)]

    for row in range(r):
        for col in range(c):
            matrix[row].append(f"{chr(97+row)}"
                          f"{chr(97 + row + col)}"
                          f"{chr(97+row)}")

    return matrix


if __name__ == "__main__":
    r, c = read_int_list_from_input()
    for i in palindromic_matrix(r,c):
        print(' '.join(i))



