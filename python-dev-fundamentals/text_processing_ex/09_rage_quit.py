data = input().upper()
collection, current, sum_digits = '', '', ''
index = 0

while True:
    try:
        if not data[index].isdigit():
            current += data[index]
            index += 1
        else:
            for j in range(index, len(data)):
                if not data[j].isdigit():
                    break
                else:
                    sum_digits += str(data[j])
                    index += 1
            collection += current * int(sum_digits)
            current, sum_digits = '', ''
    except:
        break

print(f'Unique symbols used: {len(set(collection))}')
print(collection)