line = input()
total_strenght = 0

i = 0
while i < len(line):
    ch = line[i]

    if ch == ">":
        strenght = int(line[i + 1])
        total_strenght += strenght
    else:
        if total_strenght > 0:
            line = line[:i] + line[i + 1:]
            i -= 1
            total_strenght -= 1
    i += 1

print(line)