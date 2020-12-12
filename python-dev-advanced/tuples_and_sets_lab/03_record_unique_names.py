def unique_names(n=int(input())):
    return '\n'.join(set([input() for el in range(n)]))

print(unique_names())