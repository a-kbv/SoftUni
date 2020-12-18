
def is_num_valid(number):
    return len([True for d in range(2,11) if number % d == 0]) > 0

start, end = int(input()), int(input())
print([x for x in range(start, end + 1) if is_num_valid(x)])
