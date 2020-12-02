from collections import deque

def solve():
    people = input().split()
    toss = int(input())
    players = deque(people)


    while len(players) > 1:

        for i in range(1, toss):
            players.append(players[i])

        else:
            print(f"Removed {players.popleft()}")
            person = players.popleft()

    print(f'Last is {players.pop()}')

solve()