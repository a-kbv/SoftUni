from collections import deque

def solve():
    main_list =[]
    lists, elements = [int(el) for el in input().split(', ')]

    for _ in range(lists):
        line = deque(input().split(', '))
        main_list.append([int(line.popleft()) for el in range(elements) if len(line)])

    print([sum([sum(el) for el in main_list])][0])
    print(main_list)

solve()