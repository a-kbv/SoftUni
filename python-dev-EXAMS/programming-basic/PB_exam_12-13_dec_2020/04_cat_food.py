def cat_food():
    group_1 = 0
    group_2 = 0
    group_3 = 0
    kg_food_price = 12.45
    gramms_food = 0

    for _ in range(int(input())):
        food = int(input())
        gramms_food += food
        if 100 <= food < 200:
            group_1 += 1
        elif 200 <= food < 300:
            group_2 += 1
        elif 300 <= food < 400:
            group_3 += 1

    kg_food = gramms_food / 1000
    return f"Group 1: {group_1} cats.\n"\
           f"Group 2: {group_2} cats.\n"\
           f"Group 3: {group_3} cats.\n"\
            f"Price for food per day: {(kg_food * kg_food_price):.2f} lv."

print(cat_food())