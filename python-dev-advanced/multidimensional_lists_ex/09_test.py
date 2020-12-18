#   FITNESS CARD

sport = ('Gym', 'Boxing', 'Yoga', 'Zumba', 'Dances', 'Pilates')
man = (42, 41, 45, 34, 51, 39)
woman = (35, 37, 42, 31, 53, 37)
budget, sex, y_o, sport_i = float(input()), input(), int(input()), input()

sum = 0

for i in range(len(sport)):
    if sport_i == sport[i]:
        if y_o > 19:
            if sex == "m":
                sum = man[i]
            elif sex == "f":
                sum = woman[i]
        else:
            if sex == "m":
                sum = man[i] * 0.8
            elif sex == "f":
                sum = woman[i] * 0.8

if budget >= sum:
    print(f"You purchased a 1 month pass for {sport_i}.")
else:
    print(f"You don't have enough money! You need ${sum - budget:.2f} more.")