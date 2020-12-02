# REPEAT STRINGS
strings = input().split(" ")
res = ''

for word in strings:
    res += word * len(word)
print(res)