cards = input().split()

data = input()
moves = 0
while not data == 'end':

    moves += 1
    index_1, index_2 = [int(index) for index in data.split()]

    if index_1 == index_2 or index_1 not in range(len(cards)) or index_2 not in range(len(cards)):
        print("Invalid input! Adding additional elements to the board")
        cards.insert(int(len(cards)/2), f'-{moves}a')
        cards.insert(int(len(cards) / 2), f'-{moves}a')
        data = input()
        continue

    if cards[index_1] == cards[index_2]:
        element = cards[index_1]
        print(f"Congrats! You have found matching elements - {cards[index_1]}!")
        cards.remove(element)
        cards.remove(element)
    else:
        print('Try again!')

    if len(cards) == 0:
        print(f"You have won in {moves} turns!")
        exit(0)

    data = input()

print("Sorry you lose :(")
print(' '.join(cards))
