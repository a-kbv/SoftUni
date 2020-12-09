def card_wars():
    first_player_name = input()
    second_player_name = input()

    first_player_points = 0
    second_player_points = 0

    data = input()
    while not data == 'End of game':
        first_player_card = int(data)
        second_player_card = int(input())

        if first_player_card == second_player_card:
            print("Number wars!")
            first_player_card = int(input())
            second_player_card = int(input())
            if first_player_card > second_player_card:
                print(f"{first_player_name} is winner with {first_player_points} points")
                exit(0)
            else:
                print(f"{second_player_name} is winner with {second_player_points} points")
                exit(0)
        elif first_player_card > second_player_card:
            first_player_points += first_player_card - second_player_card
        else:
            second_player_points += second_player_card - first_player_card

        data = input()

    print(f"{first_player_name} has {first_player_points} points")
    print(f"{second_player_name} has {second_player_points} points")





card_wars()