def min_max_sum(*nums):

    return f"The minimum number is {min(nums)}\n" \
           f"The maximum number is {max(nums)}\n" \
           f"The sum number is: {sum(nums)}"
print(min_max_sum(*[int(el) for el in input().split()]))

