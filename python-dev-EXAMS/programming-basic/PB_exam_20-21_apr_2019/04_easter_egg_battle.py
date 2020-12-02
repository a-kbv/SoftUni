

first_player = int(input())
second_player = int(input())

data = input()
while not data == 'End of battle':

    if data == 'one':
        second_player -= 1
    elif data == 'two':
        first_player -= 1

    if first_player == 0:
        print(f"Player one is out of eggs. Player two has {second_player} eggs left.")
        exit(0)
    elif second_player == 0:
        print(f"Player two is out of eggs. Player one has {first_player} eggs left.")
        exit(0)

    data = input()

print(f"Player one has {first_player} eggs left.")
print(f"Player two has {second_player} eggs left.")
