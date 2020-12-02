
energy = int(input())

count = 0
data = input()
while not data == 'End of battle':
    distance = int(data)
    if (energy-distance) >= 0:
        energy -= distance
        count += 1
        if count % 3 == 0:
            energy += count
    else:
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        exit()

    data = input()
print(f"Won battles: {count}. Energy left: {energy}")