import math

def tournir():
    n = int(input())
    points = int(input())
    temp_points = 0
    win = 0
    for match in range(n):
        letters = input()
        if letters == 'W':
            temp_points += 2000
            win += 1
        elif letters == 'F':
            temp_points += 1200
        elif letters == 'SF':
            temp_points += 720

    avg_points = math.floor(temp_points/n)
    percent_win = (win/n) *100

    print(f"Final points: {points+temp_points}")
    print(f"Average points: {avg_points}")
    print(f"{percent_win:.2f}%")


tournir()