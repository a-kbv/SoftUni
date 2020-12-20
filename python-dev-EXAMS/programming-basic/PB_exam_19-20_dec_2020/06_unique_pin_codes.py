def unique_pin():
    num1_max = int(input())
    num2_max = int(input())
    num3_max = int(input())

    for num1 in range(2, num1_max + 1, 2):
        for num2 in range(2, num2_max + 1):
            for num3 in range(2, num3_max + 1, 2):
                if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                    print(f"{num1} {num2} {num3}")

unique_pin()