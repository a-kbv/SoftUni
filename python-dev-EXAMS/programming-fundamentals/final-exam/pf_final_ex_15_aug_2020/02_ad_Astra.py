import re

pattern = '(#[A-Za-z\s]+#\d\d/\d\d/\d\d#\d{0,}#)|(\|[A-Za-z\s]+\|\d\d/\d\d/\d\d\|\d{0,}\|)'
message = input()
foods = re.finditer(pattern, message)
for match in foods:
    food = match[0]
    food_name = re.findall(r'[A-Za-z\s]+', food)
    print(food_name)
    print(food)