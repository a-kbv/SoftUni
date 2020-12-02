n_client = int(input())
total_sum = 0

for client in range(n_client):
    items_count = 0
    items_sum = 0

    data = input()
    while not data == "Finish":

        if data == "basket":
            items_count += 1
            items_sum += 1.50
        elif data == "wreath":
            items_count += 1
            items_sum += 3.80
        elif data == "chocolate bunny":
            items_count += 1
            items_sum += 7

        data = input()
    if items_count % 2 == 0:
        items_sum *= 0.8
    total_sum += items_sum
    print(f"You purchased {items_count} items for {items_sum:.2f} leva.")

avg_bill_per_client = total_sum/n_client
print(f"Average bill per client is: {avg_bill_per_client:.2f} leva.")
