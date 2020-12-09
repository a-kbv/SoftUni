
def darts():

    starting_points = 301
    player_name = input()
    data = input()
    multiplier = 1
    succesfull_turns = 0
    unsuccesfull_turns = 0

    while not data == 'Retire':
        zone = data
        if zone == 'Single':
            multiplier = 1
        elif zone == 'Double':
            multiplier = 2
        elif zone == 'Triple':
            multiplier = 3

        points = int(input())

        if (starting_points - (multiplier * points)) >= 0:
            starting_points -= multiplier * points
            succesfull_turns += 1
        else:
            unsuccesfull_turns += 1

        if starting_points == 0:
            print(f"{player_name} won the leg with {succesfull_turns} shots.")
            exit(0)
        data = input()
    print(f"{player_name} retired after {unsuccesfull_turns} unsuccessful shots.")
darts()