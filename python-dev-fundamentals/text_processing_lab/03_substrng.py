substr = input()
string = input()
cnt = 0
for _ in range(string.count(substr)):
    if substr in string:
        string = string.replace(substr, "")
print(string)

