# SCHOOL SUPPLIES
pen_p = 5.80
highl_p = 7.20
liter_detergent_p = 1.20

pen_c = int(input())
highl_c = int(input())
liter_detergent_c = float(input())
discount = int(input())

money_needed = ((pen_c * pen_p)+(highl_p * highl_c)+(liter_detergent_c * liter_detergent_p) ) * (1-(discount / 100))
print(f"{money_needed:.3f}")