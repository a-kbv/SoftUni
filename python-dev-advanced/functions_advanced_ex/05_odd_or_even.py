def odd_or_even(command, *nums):
    if command == "Odd":
        return sum([num for num in nums if num % 2 == 1])*len(nums)
    elif command == "Even":
        return sum([num for num in nums if num % 2 == 0])*len(nums)

print(odd_or_even(input(), *[int(num) for num in input().split()]))