
guests_count = int(input())
price_per_guest = float(input())
budget = float(input())

if 10 <= guests_count <= 15:
    price_per_guest *= 0.85
if 15 < guests_count <= 20:
    price_per_guest *= 0.8
if guests_count >20:
    price_per_guest *= 0.75

sum = guests_count * price_per_guest + 0.1 * budget
if budget >= sum:
    print(f"It is party time! {budget-sum:.2f} leva left.")
else:
    print(f"No party! {sum-budget:.2f} leva needed.")