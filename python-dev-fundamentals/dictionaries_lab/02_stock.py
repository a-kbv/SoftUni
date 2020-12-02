elements = input().split()
products = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = elements[index + 1]
    products[key] = int(value)

searched = input().split()
for item in searched:
    if item in products:
        print(f"We have {products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")