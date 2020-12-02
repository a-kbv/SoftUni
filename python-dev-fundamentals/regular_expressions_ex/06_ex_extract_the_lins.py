import re
# www\.[a-zA-Z0-9]+(\-)*[a-zA-Z0-9]+\.[a-zA-Z0-9]+((\.)[a-zA-Z0-9]+)*
# (?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+

# TODO 80/100

pattern = r"www\.[a-zA-Z0-9]+(\-)*[a-zA-Z0-9]+\.[a-zA-Z0-9]+(\.)*[a-zA-Z0-9]+"


data = input()
while not data == "":
    res = re.finditer(pattern, data)
    for el in res:
        print(el[0])
    data = input()
