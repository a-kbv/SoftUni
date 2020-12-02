from collections import deque

def solve():
    people = input().split()
    toss = int(input())
    players = deque(people)


    while len(players) > 1:

        for _ in range(1, toss):
            players.append(players.popleft())

        print(f"Removed {players.popleft()}")

    print(f'Last is {players.pop()}')

solve()