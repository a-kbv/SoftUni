def shoot(targets, index):
    temp = targets[index]
    if not targets[index] == -1:
        targets[index] = -1
    for el in range(len(targets)):
        if targets[el] > temp and not targets[el] == -1:
            targets[el] -= temp
        elif targets[el] <= temp and not targets[el] == -1:
            targets[el] += temp
    return targets

targets = [int(el) for el in input().split()]
shot_target = 0

data = input()
while not data == 'End':
    index = int(data)
    if index < len(targets):
        targets = shoot(targets, index)
        shot_target += 1

    data = input()

print(f'Shot targets: {shot_target} -> {" ".join(str(el) for el in targets)}')