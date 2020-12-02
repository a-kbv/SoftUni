import math
guests = int(input())
budget = int(input())
# 1 cosunac and 6 eggs for 3 ppl
cos_price = 4
egg_price = 0.45

cos_count = math.ceil(guests/3)
egg_count = guests * 2

total_sum = cos_count * cos_price + egg_count*egg_price

if budget >= total_sum:
    print(f"Lyubo bought {cos_count} Easter bread and {egg_count} eggs.")
    print(f"He has {(budget-total_sum):.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {(total_sum-budget):.2f} lv. more.")
