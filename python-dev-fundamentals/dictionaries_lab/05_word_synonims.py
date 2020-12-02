n = int(input())
dict = {}

for i in range(n):
    key = input()
    value = input()
    if key not in dict:
        dict[key] = value
    elif key in dict:
        dict[key] += f", {value}"

for key in dict:
    print(f"{key} - {dict[key]}")