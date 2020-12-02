import math
used_sugars= 0
used_flours = 0
max_sugar = 0
max_flour = 0

cosunacs_count = int(input())
for each in range(cosunacs_count):
    used_sugar = int(input()) # g
    used_flour = int(input()) # g
    used_sugars+= used_sugar
    used_flours+= used_flour
    if used_sugar > max_sugar: max_sugar = used_sugar
    if used_flour > max_flour: max_flour = used_flour

sugar_pack = math.ceil(used_sugars/950) #950 #g
flour_pack = math.ceil(used_flours/750) #750 #g
print(f"Sugar: {sugar_pack}")
print(f"Flour: {flour_pack}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")