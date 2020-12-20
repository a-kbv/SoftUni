
def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

def palindromic_matrix(r,c):

    # matrix = [[]*r for _ in range(r)]
    # for row in range(r):
    #     for col in range(c):
    #         matrix[row].append(f"{chr(97+row)}"
    #                       f"{chr(97 + row + col)}"
    #                       f"{chr(97+row)}")

    return [[f"{chr(row)}{chr(row + col)}{chr(row)}" for col in range(c)]for row in range(97, 97+r)]


if __name__ == "__main__":
    r, c = read_int_list_from_input()
    for i in palindromic_matrix(r,c):
        print(' '.join(i))



