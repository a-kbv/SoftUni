days = int(input())
count_days  = 0
sum = 0
win = 0
lose = 0
win_day = 0
lose_day = 0
total_sum = 0
for day in range(1,days+1):
    while True:
        sport = input()
        if sport == "Finish":
            count_days += 1
            break
        w_l = input()
        if w_l == "win":
            sum += 20
            win += 1
        elif w_l == "lose":
            lose += 1
    if win > lose:
        total_sum += (sum * 1.1)
        win = 0
        lose = 0
        sum = 0
        win_day += 1
    else:
        lose_day += 1
        total_sum += sum
        win = 0
        lose = 0
        sum = 0
if win_day > lose_day:
    total_sum *= 1.2
    print(f"You won the tournament! Total raised money: {total_sum:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_sum:.2f}")