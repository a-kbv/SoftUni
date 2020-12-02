def char_position(letter):
    char = letter.lower()
    return (ord(char) + 1) - 97


data = input().split()
total_sum = 0


for el in data:
    sums = 0
    fchar = el[0]
    lchar = el[-1]
    num = el[1:-1]

    if fchar.isupper():
        divider = char_position(fchar)
        sums += int(num)/divider
    else:
        multipler = char_position(fchar)
        sums += int(num)*multipler

    if lchar.isupper():
        subtractor = char_position(lchar)
        sums -= subtractor
    else:
        additor = char_position(lchar)
        sums += additor
        pass

    total_sum += sums

print(f'{total_sum:.2f}')
