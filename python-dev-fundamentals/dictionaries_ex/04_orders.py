data = input()
products = {}

while not data == "buy":
    key, value, quantity = data.split()
    value = float(value)
    quantity = int(quantity)
    if key not in products:
        products[key] = [value,quantity]
    else:
        if products[key][0] != value:
            products[key][0] = value
            products[key][1] += quantity
        else:
            products[key][1] += (quantity)

    data = input()
for prod in products:
    print(f"{prod} -> {((products[prod][0]) * (products[prod][1])):.2f}")