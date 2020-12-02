
eggs = int(input())

data = input()
cnt_sold = 0
while not data == 'Close':
    count = int(input())
    if data == 'Buy':
        if count > eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {eggs}.")
            exit(0)

        eggs -= count
        cnt_sold += count

    elif data == "Fill":
        eggs += count

    data = input()

print(f"Store is closed!")
print(f"{cnt_sold} eggs sold.")