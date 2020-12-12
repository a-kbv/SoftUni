def christmas_gifts():
    adults = 0
    kids = 0
    toys_money = 0
    sweaters_money = 0

    data = input()
    while not data == "Christmas":
        yo = int(data)
        if yo <= 16:
            kids += 1
            toys_money += 5
        else:
            adults += 1
            sweaters_money += 15

        data = input()

    return f"Number of adults: {adults}\n"\
           f"Number of kids: {kids}\n"\
           f"Money for toys: {toys_money}\n"\
           f"Money for sweaters: {sweaters_money}"

print(christmas_gifts())