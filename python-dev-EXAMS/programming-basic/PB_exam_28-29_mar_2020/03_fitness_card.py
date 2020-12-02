#   FITENSS CARD

sport = ['Gym', 'Boxing', 'Yoga', 'Zumba', 'Dances', 'Pilates']
man = [42, 41, 45, 34, 51, 39]
woman = [35, 37, 42, 31, 53, 37]

budget = float(input())
sex = input()
y_o = int(input())
sport_i = input()

sum = 0

if sex == "m": # man
    if y_o > 19:
        if sport_i == sport[0]:
            sum = man[0]
        if sport_i == sport[1]:
            sum = man[1]
        if sport_i == sport[2]:
            sum = man[2]
        if sport_i == sport[3]:
            sum = man[3]
        if sport_i == sport[4]:
            sum = man[4]
        if sport_i == sport[5]:
            sum = man[5]
    else:
        if sport_i == sport[0]:
            sum = man[0] * 0.8
        if sport_i == sport[1]:
            sum = man[1] * 0.8
        if sport_i == sport[2]:
            sum = man[2] * 0.8
        if sport_i == sport[3]:
            sum = man[3] * 0.8
        if sport_i == sport[4]:
            sum = man[4] * 0.8
        if sport_i == sport[5]:
            sum = man[5] * 0.8
elif sex == "f": # woman
    if y_o > 19:
        if sport_i == sport[0]:
            sum = woman[0]
        if sport_i == sport[1]:
            sum = woman[1]
        if sport_i == sport[2]:
            sum = woman[2]
        if sport_i == sport[3]:
            sum = woman[3]
        if sport_i == sport[4]:
            sum = woman[4]
        if sport_i == sport[5]:
            sum = woman[5]
    else:
        if sport_i == sport[0]:
            sum = woman[0] * 0.8
        if sport_i == sport[1]:
            sum = woman[1] * 0.8
        if sport_i == sport[2]:
            sum = woman[2] * 0.8
        if sport_i == sport[3]:
            sum = woman[3] * 0.8
        if sport_i == sport[4]:
            sum = woman[4] * 0.8
        if sport_i == sport[5]:
            sum = woman[5] * 0.8

if budget >= sum:
    print(f"You purchased a 1 month pass for {sport_i}.")
else:
    print(f"You don't have enough money! You need ${sum - budget:.2f} more.")