def swap(index_1, index_2, array):
    array[index_1], array[index_2] = array[index_2], array[index_1]
    return array

def multiply(index_1, index_2, array):
    temp_1 = array[index_1]
    temp_2 = array[index_2]

    res = temp_1 * temp_2
    array.pop(index_1)
    array.insert(index_1, res)
    return array

def decrease(array):
    array = [(el)-1 for el in array]
    return array

array = input().split()
array = [int(el) for el in array]

data = input()

while not data == 'end':
    data = data.split()
    do = data[0]

    if do == 'swap':
        index_1 = int(data[1])
        index_2 = int(data[2])
        array = swap(index_1, index_2, array)

    if do == 'multiply':
        index_1 = int(data[1])
        index_2 = int(data[2])
        array = multiply(index_1, index_2, array)

    if do == 'decrease':
        array = decrease(array)

    data = input()
print(*array, sep=', ')

