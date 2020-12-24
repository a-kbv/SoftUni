def neg_vs_pos(*nums):
    sum_pos = sum([num for num in nums if num >= 0])
    sum_neg = sum([num for num in nums if num < 0])

    if abs(sum_neg) > sum_pos:
        return f"{sum_neg}\n" \
               f"{sum_pos}\n" \
               f"The negatives are stronger than the positives"

    return f"{sum_neg}\n" \
               f"{sum_pos}\n" \
               f"The positives are stronger than the negatives"
print(neg_vs_pos(*[int(num) for num in input().split()]))