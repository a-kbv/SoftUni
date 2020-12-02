from collections import deque

def solve():
    water = int(input())
    people = deque()

    while True:
        data = input()
        if data == 'Start':
            break
        people.append(data)

    while True:
        data = input().split(' ')
        if data[0] == 'End':
            print(f'{water} liters left')
            break
        elif data[0] == 'refill':
            water += int(data[1])
        else:
            person_water = int(data[0])
            person = people.popleft()

            if person_water <= water:
                water -= person_water
                print(f'{person} got water')
            else:
                print(f'{person} must wait')

solve()