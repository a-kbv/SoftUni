text = input()
digits = ''
letters = ''
other_symbols = ''

for char in text:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        other_symbols += char

print(digits)
print(letters)
print(other_symbols)