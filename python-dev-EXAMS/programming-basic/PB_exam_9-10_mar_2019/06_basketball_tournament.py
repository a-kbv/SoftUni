
def tournir():

    game_n = 0
    total_matches = 0
    win = 0
    lose = 0

    data = input()

    while not data == "End of tournaments":
        t_name = data
        t_n = int(input())
        total_matches += t_n

        for _ in range(t_n):
            game_n += 1
            ally = int(input())
            enemy = int(input())
            if ally > enemy:
                print(f"Game {game_n} of tournament {t_name}: win with {ally - enemy} points.")
                win += 1
            else:
                print(f"Game {game_n} of tournament {t_name}: lost with {enemy - ally} points.")
                lose += 1

        data = input()
        game_n = 0

    print(f"{((win/total_matches)*100):.2f}% matches win")
    print(f"{((lose/total_matches)*100):.2f}% matches lost")


tournir()