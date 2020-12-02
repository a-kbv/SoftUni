
numbers = [int(el) for el in input().split()]

greater_than_avg = [(num) for num in numbers if num > sum(numbers) / len(numbers)]

if len(greater_than_avg) == 0:
    print('No')
else:
    greater_than_avg.sort()
    greater_than_avg = greater_than_avg[::-1]
    print(*greater_than_avg[:5])
