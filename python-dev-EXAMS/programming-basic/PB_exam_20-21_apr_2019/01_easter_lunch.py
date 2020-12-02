#EASTER LUNCH

kozuncas_count = int(input())
eggs_count = int(input())
cookies_count = int(input())

sum = kozuncas_count * 3.20 + eggs_count * 4.35+\
    cookies_count * 5.40 + eggs_count * 12 * 0.15
print(f"{sum:.2f}")