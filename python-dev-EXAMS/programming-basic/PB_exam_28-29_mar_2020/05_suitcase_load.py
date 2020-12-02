capacity = float(input())
space = 0
count = 0
total_count =0
while True:
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    count += 1
    if count == 3:
        space += (float(command) + (0.1 * (float(command))))
        count = 0
    else:
        space += (float(command))
    if space > capacity:
        print("No more space!")
        break
    total_count += 1
print(f"Statistic: {total_count} suitcases loaded.")

