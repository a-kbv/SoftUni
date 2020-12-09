def football_match():
    cnt_win = 0
    cnt_lost = 0
    cnt_draw = 0
    for i in range(3):
        temp = [int(el) for el in input().split(':')]

        if temp[0] > temp[1]:
            cnt_win += 1
        elif temp[0] < temp[1]:
            cnt_lost += 1
        elif temp[0] == temp[1]:
            cnt_draw += 1
    return f'Team won {cnt_win} games.\n' \
           f'Team lost {cnt_lost} games.\n' \
           f'Drawn games: {cnt_draw}'
print(football_match())