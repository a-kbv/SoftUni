while True:
    data = input().split()
    is_found = False

    for index in range(0, len(data), 2):
        quantity = int(data[index])
        item = data[index + 1].lower()

        if item in key_materials:
            key_materials[item] += quantity
        else:
            if item not in junks:
                junks[item] = quantity
            else:
                junks[item] += quantity

        for key, value in key_materials.items():
            if value >= 250:
                print(f'{mapper[key]} obtained!')
                key_materials[key] -= 250
                is_found = True
                break
        if is_found:
            break
    if is_found:
        break

ordered_key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
for item, quantity in ordered_key_materials.items():
    print(f'{item}: {quantity}')

    # sort only index alphabetically ascending
ordered_junks = sorted(junks.items(), key=lambda x: x[0])

for junk_item, junk_quantity in ordered_junks:
    print(f'{junk_item}: {junk_quantity}')