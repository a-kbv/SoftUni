import math
tennis_racket_price = float(input())
tennis_racket_count = int(input())
trousers_count = int(input())
trousers_price = (1/6) * tennis_racket_price
sum = tennis_racket_price * tennis_racket_count + trousers_count * trousers_price
other_equipment = 0.2 * sum
print(f"Price to be paid by Djokovic {math.floor((1/8)*(sum+other_equipment))}")
print(f"Price to be paid by sponsors {math.ceil((7/8)*(sum+other_equipment))}")

