type_customer = ["special", "regular"]
data = input()
total_sum_wo_tax = 0

while not data in type_customer:

    num = float(data)

    if num < 0:
        print("Invalid price!")

    else:
        total_sum_wo_tax += num
    data = input()

taxes = 0.2 * total_sum_wo_tax

if total_sum_wo_tax == 0:
    print("Invalid order!")

elif data == "special":
    total_sum = (taxes + total_sum_wo_tax) * 0.9
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_sum_wo_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_sum:.2f}$")

elif data == "regular":
    total_sum = taxes + total_sum_wo_tax
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_sum_wo_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_sum:.2f}$")