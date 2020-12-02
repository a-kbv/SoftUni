min_walk = int(input())
count_walks = int(input())
kcal = int(input())

used_kcal = min_walk * count_walks * 5
if used_kcal >= 1/2*kcal:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {used_kcal}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {used_kcal}.")
