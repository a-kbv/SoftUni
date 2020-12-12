def parking_lot(n=int(input())):
    cars = set()

    for _ in range(n):
        data = input().split(', ')
        if data[0] == 'IN':
            cars.add(data[1])
        else:
            cars.remove(data[1])
    if cars:
        return '\n'.join(cars)
    return 'Parking Lot is Empty'
print(parking_lot())