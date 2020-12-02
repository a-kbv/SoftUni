collored_eggs_count = int(input())

egg_dict = {'red': 0, 'orange': 0, 'blue': 0, 'green': 0}

for egg in range(collored_eggs_count):
    color = input().strip()
    egg_dict[color] += 1


max_key = max(egg_dict, key=lambda k: egg_dict[k])
print(f"Red eggs: {egg_dict['red']}")
print(f"Orange eggs: {egg_dict['orange']}")
print(f"Blue eggs: {egg_dict['blue']}")
print(f"Green eggs: {egg_dict['green']}")
print(f"Max eggs: {egg_dict[max_key]} -> {max_key}")


