c_bcoin = int(input())
c_yuan = float(input())
commisions = float(input())

bcoin = 1168 # bgn
usd = 1.76 # bgn
eur = 1.95 # bgn

total_usd = c_yuan * (0.15 * usd)
total_lv = (c_bcoin * bcoin) + total_usd
total_eur = total_lv / 1.95
sum_in_eur_and_commision = total_eur * (1-(commisions/100))
print(f"{(sum_in_eur_and_commision):.2f}")

