def competition():
    dancers_count = int(input())
    points_count = float(input())
    season = input()
    country = input()

    money = dancers_count * points_count
    charity = 0

    if country == "Abroad":
        money *= 1.5

        if season == "summer":
            money *= (1 - 0.10)
        else:
            money *= (1 - 0.15)
    else:

        if season == "summer":
            money *= (1-0.05)
        else:
            money *= (1-0.08)

    charity = money * 0.75
    left_money = money - charity
    money_per_dancer = left_money / dancers_count

    return f"Charity - {charity:.2f}\nMoney per dancer - {money_per_dancer:.2f}"

print(competition())