import re

string_input = input()

valid_pattern = r'([=]|[/])[A-Z][A-Za-z]{2,}\1'

matched = re.finditer(valid_pattern, string_input)

matched_list = [el[0].strip('/').strip('=') for el in matched]

travel_points = sum((len(el) for el in matched_list))

print(f"Destinations: {', '.join(matched_list)}")
print(f"Travel Points: {travel_points}")

# FFFFFF**** NOONE SAID THE SECOND LETTER CAN BE UPPERCASE TOO :X

