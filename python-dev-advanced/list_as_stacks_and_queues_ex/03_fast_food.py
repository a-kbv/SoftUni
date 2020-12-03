from collections import deque

def solve(quantity):
    orders = [int(el) for el in input().split()]
    orders = deque(orders)
    is_p = True
    while orders:
        if is_p:
            print(max(orders))
            is_p = False

        if quantity >= (orders[0]):
                quantity -= (orders.popleft())

        else:
            print(f'Orders left: {" ".join(map(str,orders))}')
            exit(0)
    print('Orders complete')


solve(int(input()))

