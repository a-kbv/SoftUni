import re

phone_nums = input()
regex = r"(\+359\s[2]\s\d{3}\s\d{4})|(\+359\-[2]\-\d{3}\-\d{4})\b"
valid_phone_nums = re.finditer(regex, phone_nums)
valid_phone_nums= [el.group(0) for el in valid_phone_nums]
print(', '.join(valid_phone_nums))


