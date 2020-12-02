import re

pattern = r">>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"

total_money_spend = 0

text = input()

print("Bought furniture:")

while not text == "Purchase":
    match = re.fullmatch(pattern, text)
    if match is None:
        text = input()
        continue
    item = match[1]
    price = float(match[2])
    quantity = int(match[4])
    total_money_spend += price * quantity

    print(item)
    text = input()

print(f"Total money spend: {total_money_spend:.2f}")