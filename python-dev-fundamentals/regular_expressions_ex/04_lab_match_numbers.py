import re

data = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
numbers = re.finditer(pattern, data)
numbers= [el.group(0) for el in numbers]
print(' '.join(numbers))