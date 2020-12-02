houses = [int(el) for el in input().split('@')]

command = input()
position = 0

while not command == "Love!":
    lenght = int(command.split()[1])
    position += lenght
    if position >= len(houses):
        position = 0
    if houses[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        houses[position] -= 2
        if houses[position] == 0:
            print(f"Place {position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {position}.")

if sum(houses) == 0:
    print(f"Mission was successful.")
else:
    count = len([el for el in houses if el >0])
    print(f"Cupid has failed {count} places.")