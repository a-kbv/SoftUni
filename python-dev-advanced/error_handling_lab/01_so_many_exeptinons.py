def read_input():
    return [int(el) for el in input().split(", ")]

def calculate(numbers_list):
    result = 1
    n = len(numbers_list)
    for number in numbers_list:
        if number <= 5:
            result *= number
        elif 5 < number <= 10:
            result /= number
    return int(result)

if __name__ == "__main__":
    numbers_list = read_input()
    print(calculate(numbers_list))
