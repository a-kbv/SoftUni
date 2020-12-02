flour_price_per_kg = float(input())
flour_kg = float(input())

sugar_kg = float(input())
sugar_price_per_kg = (1-0.25) * flour_price_per_kg

egg_boxes = int(input())
egg_box_price = 1.1* flour_price_per_kg

yeast_boxes = int(input())
yeast_box_price = (1-0.8)* sugar_price_per_kg

sum = flour_kg * flour_price_per_kg + sugar_kg*sugar_price_per_kg+\
    egg_boxes * egg_box_price + yeast_boxes * yeast_box_price

print(f"{sum:.2f}")