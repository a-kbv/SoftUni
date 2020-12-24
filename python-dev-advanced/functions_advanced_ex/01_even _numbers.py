def even_nums(*nums):
    return [el for el in nums if el % 2 == 0]

print(even_nums(*[int(el) for el in input().split()]))