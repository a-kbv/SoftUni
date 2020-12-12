def sum_ascii_and_divide(name, divisor):
    sums = 0
    for el in name:
        sums += ord(el)
    return sums//divisor

def battle_o_names(n=int(input())):
    odd_numbers = set()
    even_numbers = set()
    for divider in range(1, n+1):
        name = input()
        sums = sum_ascii_and_divide(name, divider)
        if sums % 2 ==0 :
            even_numbers.add(sums)
        else:
            odd_numbers.add(sums)

    odd_sum = sum(odd_numbers)
    even_sum = sum(even_numbers)

    if odd_sum == even_sum:
        union_values = odd_numbers.union(even_sum)
        print(', '.join([str(x) for x in union_values]))
    elif odd_sum > even_sum:
        different_values = odd_numbers.difference(even_numbers)
        print(', '.join([str(x) for x in different_values]))
    else:
        symetric_values = odd_numbers.symmetric_difference(even_numbers)
        print(', '.join([str(x) for x in symetric_values]))

battle_o_names()