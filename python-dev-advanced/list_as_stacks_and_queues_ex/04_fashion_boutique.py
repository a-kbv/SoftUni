from collections import deque

def solve():
    box_capacity = [int(el) for el in input().split()]
    items = deque(box_capacity)
    box_capacity = int(input())
    sum = 0
    number_of_boxes = 1

    while items:
        sum += items[-1]
        if sum <= box_capacity:
            items.pop()
        else:
            number_of_boxes += 1
            sum = 0
    return number_of_boxes

print(solve())

