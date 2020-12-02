def shoot(targets, index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets

def add(targets, index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")
    return targets

def strike(targets, index, radius):
    left_index = index - value
    right_index = index + value

    if left_index >= 0 and right_index < len(targets):
        targets = targets[:left_index] + targets[right_index+1:]
    else:
        print("Strike missed!")
    return targets

targets = [int(el) for el in input().split()]

data = input()
while not data == 'End':
    data = data.split()
    command, index, value = data[0], int(data[1]), int(data[2])

    if command == 'Shoot':
        targets = shoot(targets, index, value)
    if command == 'Add':
        targets = add(targets, index, value)
    if command == 'Strike':
        targets = strike(targets, index, value)

    data = input()
print('|'.join(map(str, targets)))