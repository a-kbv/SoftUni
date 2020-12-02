elements = input()
products = {}

while not elements == "statistics":
    elements = elements.split(": ")
    key = elements[0]
    value = int(elements[1])
    if key not in products:
        products[key] = value
    else:
        products[key] += value

    elements = input()
print(f"Products in stock:")
for prod in products:
    print(f"- {prod}: {products[prod]}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")