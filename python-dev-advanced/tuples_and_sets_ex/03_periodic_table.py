def unique_chem_el(n=int(input())):
    periodic_table = set()
    while n:
        data = input().split(' ')
        for el in range(len(data)):
            periodic_table.add(data[el])
        n -= 1
    return '\n'.join(periodic_table)

print(unique_chem_el())