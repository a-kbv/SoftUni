from collections import deque

def crossroads():
    green_time = int(input())
    window_time = int(input())
    crashed = False

    cars = deque()
    counter = 0

    data = input()
    while not data == "END":
        if data == "green":
            green_timer = green_time
            # pass on green
            if cars:
                copy = cars.popleft()
                current_car = deque(copy)
                while green_timer:
                    if not current_car:
                        if cars:
                            copy = cars.popleft()
                            current_car = deque(copy)
                        else:
                            break
                    current_car.popleft()
                    green_timer -= 1
            # pass on yellow if you can if still in crossroad
                if current_car:
                    window_timer = window_time
                    while window_timer and current_car:
                        current_car.popleft()
                        window_timer -= 1
                if current_car:
                    crashed = True
                    print(f"A crash happened!")
                    print(f"{copy} was hit at {current_car.popleft()}.")
                    break
        else:
            cars.append(data)
            counter += 1
        data = input()

    if not crashed:
        print("Everyone is safe.")
        print(f"{counter - len(cars)} total cars passed the crossroads.")


crossroads()