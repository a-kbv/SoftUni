def even_odd(*nums):
    nums = list(nums)
    if nums[-1] == "even":
        nums.pop()
        return [num for num in nums if num % 2 == 0]
    nums.pop()
    return [num for num in nums if num % 2 == 1]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
