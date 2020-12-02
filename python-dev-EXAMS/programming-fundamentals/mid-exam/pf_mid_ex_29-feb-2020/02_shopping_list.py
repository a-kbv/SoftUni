def urgent(grocery,data):
    if not data[1] in grocery:
        grocery.insert(0, data[1])
        return grocery
    return grocery

def unnecessary(grocery, data):
    if data[1] in grocery:
        grocery.remove(data[1])
        return grocery
    return grocery

def correct(grocery, data):
    if data[1] in grocery:
        index = grocery.index(data[1])
        grocery[index] = data[2]
        return grocery
    return grocery

def rearrange(grocery, data):
    if data[1] in grocery:
        grocery.remove(data[1])
        grocery.append(data[1])
        return grocery
    return grocery

grocery = input().split('!')

data = input()
while not data == 'Go Shopping!':
    data = data.split()
    if data[0] == 'Urgent':
        grocery = urgent(grocery, data)
    elif data[0] == 'Unnecessary':
        grocery = unnecessary(grocery, data)
    elif data[0] == 'Correct':
        grocery = correct(grocery, data)
    elif data[0] == 'Rearrange':
        grocery = rearrange(grocery, data)

    data = input()

print(', '.join(grocery))
