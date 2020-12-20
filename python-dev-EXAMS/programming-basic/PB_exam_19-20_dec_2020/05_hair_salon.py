def hair_salon(needed=int(input())):
    data = input()
    money_made = 0
    while not data == "closed":

        data_1 = input()
        if data == "haircut":
            if data_1 == "mens":
                money_made += 15
            elif data_1 == "ladies":
                money_made += 20
            elif "kids":
                money_made += 10
        elif data == "color":
            if data_1 == "touch up":
                money_made += 20
            elif "full color":
                money_made += 30

        if money_made >= needed:
            print(f"You have reached your target for the day!\n"
                  f"Earned money: {money_made}lv.")
            exit()
        data = input()

    print(f"Target not reached! You need {(needed-money_made)}lv. more.\n"
          f"Earned money: {money_made}lv.")

hair_salon()