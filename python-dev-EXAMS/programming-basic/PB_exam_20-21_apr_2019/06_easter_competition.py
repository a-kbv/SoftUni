n_cosunacs = int(input())
max_points = 0
winning_baker = ""

for cos in range(n_cosunacs):
    baker_name = input()
    points = 0

    data = input()
    while not data == 'Stop':
        points += int(data)
        data = input()

    print(f"{baker_name} has {points} points.")

    if points > max_points:
        print(f"{baker_name} is the new number 1!")
        max_points = points
        winning_baker = baker_name

print(f"{winning_baker} won competition with {max_points} points!")


