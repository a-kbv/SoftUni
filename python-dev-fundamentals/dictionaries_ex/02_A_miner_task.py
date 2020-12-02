cnt = 0
dict = {}

data = input()
while not data == "stop":
    value = int(input())
    cnt += 1
    if data not in dict:
        dict[data] = value
    else:
        dict[data] += value
    data = input()
for key in dict:
    print(f"{key} -> {dict[key]}")