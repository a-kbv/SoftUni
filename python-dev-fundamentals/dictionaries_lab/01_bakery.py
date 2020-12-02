data = input().split()
prod = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    prod[key] = value

print(prod)