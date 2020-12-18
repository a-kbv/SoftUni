
def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

def primary_diagona(matrix,n):
    return [matrix[r][r] for r in range (n)]

def secondary_diagonal(matrix,n):
    return [matrix[r][n-1-r] for r in range(n)]

if __name__ == "__main__":
    n = int(input())
    matrix = [read_int_list_from_input(', ') for _ in range(n)]
    pd = primary_diagona(matrix,n)
    sd = secondary_diagonal(matrix,n)
    print(f"First diagonal: {', '.join(map(str, pd))}. Sum: {sum(pd)}")
    print(f"Second diagonal: {', '.join(map(str, sd))}. Sum: {sum(sd)}")
