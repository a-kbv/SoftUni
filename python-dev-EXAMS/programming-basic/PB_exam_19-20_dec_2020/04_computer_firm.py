def pc_company(n=int(input())):
    rating_dict = {2: 0, 3: 0.5, 4: 0.70, 5: 0.85, 6: 1}
    sold = 0
    ratings = 0

    for _ in range(n):
        rating = input()
        pc_sold = int(rating[:-1])
        num = int(rating[-1])
        ratings += num
        sold += rating_dict[num] * pc_sold

    avg_rating = ratings/n

    return f"{sold:.2f}\n{avg_rating:.2f}"

print(pc_company())
