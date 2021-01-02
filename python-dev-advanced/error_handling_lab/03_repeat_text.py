def read_input():
    text = input()
    times = int(input())
    return (text, times)

def solve():
    try:
        (text, times) = read_input()
    except ValueError as err:
        return (err)
    return text * times


print(solve())
