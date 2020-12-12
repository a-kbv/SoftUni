def unique_el_of_two_sets():
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    set_1 = set(input() for el in range(n))
    set_2 = set(input() for el in range(m))
    return '\n'.join(set_1.intersection(set_2))

print(unique_el_of_two_sets())