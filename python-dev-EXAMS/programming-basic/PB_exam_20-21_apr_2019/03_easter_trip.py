destination = input()
dates = input()
nights = int(input())

France = 0
Italy = 0
Germany = 0
dest = 0


if dates == '21-23':
    France, Italy, Germany = 30,28,32
elif dates == '24-27':
    France, Italy, Germany = 35,32,37
elif dates == '28-31':
    France, Italy, Germany = 40,39,43

if destination == 'France':
    dest = France
elif destination =='Germany':
    dest = Germany
elif destination == 'Italy':
    dest = Italy

print(f"Easter trip to {destination} "
      f": {(dest * nights):.2f} leva.")