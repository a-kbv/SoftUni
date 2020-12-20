def football_kit(tshirt_price=float(input()), money_needed=float(input())):
    short_price = tshirt_price * 0.75
    socks_price = short_price * 0.20
    buttonki_price = (tshirt_price + short_price) * 2

    total = (tshirt_price + short_price + socks_price + buttonki_price) * (1-0.15)

    if total >= money_needed:
        return f"Yes, he will earn the world-cup replica ball!\nHis sum is {total:.2f} lv."
    else:
        return f"No, he will not earn the world-cup replica ball.\nHe needs {(money_needed - total):.2f} lv. more."

print(football_kit())