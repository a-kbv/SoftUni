days = int(input())
quantity = float(input())
eaten_by_dog = 0
ebd = 0
eaten_by_cat = 0
ebc = 0
counter = 0
biscuit = 0
for i in range(1, days+1):
    ebd = int(input())
    ebc = int(input())
    eaten_by_dog += ebd
    eaten_by_cat += ebc
    counter += 1
    if counter == 3:
        biscuit += 0.1 * (ebd + ebc)
        counter = 0

total_eaten_food = eaten_by_dog + eaten_by_cat

print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{((total_eaten_food / quantity) * 100):.2f}% of the food has been eaten.")
print(f"{((eaten_by_dog / total_eaten_food) * 100):.2f}% eaten from the dog.")
print(f"{((eaten_by_cat / total_eaten_food) * 100):.2f}% eaten from the cat.")