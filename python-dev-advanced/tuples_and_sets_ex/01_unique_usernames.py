def unique_names():
    return set(input() for _ in range(int(input())))

print('\n'.join(unique_names()))