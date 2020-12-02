from collections import deque

def solve(people):
    toss = int(input())
    people = deque(people)


    while len(people) > 1:

        for _ in range(1, toss):
            people.append(people.popleft())

        print(f"Removed {people.popleft()}")

    print(f'Last is {people.pop()}')

solve(input().split())