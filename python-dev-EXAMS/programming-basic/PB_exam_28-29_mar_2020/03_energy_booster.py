fruit = input()
size = input()
count = int(input())
sum = 0
if fruit == "Watermelon":
    if size == "small":
        sum = count * 2 * 56.00
    elif size == "big":
        sum = count * 5 * 28.70
if fruit == "Mango":
    if size == "small":
        sum = count * 2 * 36.66
    elif size == "big":
        sum = count * 5 * 19.60
if fruit == "Pineapple":
    if size == "small":
        sum = count * 2 * 42.10
    elif size == "big":
        sum = count * 5 * 24.80
if fruit == "Raspberry":
    if size == "small":
        sum = count * 2 * 20.00
    elif size == "big":
        sum = count * 5 * 15.20
if sum >=400 and sum <=1000:
    sum *= 0.85
elif sum >1000:
    sum *= 0.5
print(f"{sum:.2f} lv.")
