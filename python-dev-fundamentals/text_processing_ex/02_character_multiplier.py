strings = input().split()

sums = 0

smallest = strings[0]
longest = strings[1]

if len(strings[1]) < len(strings[0]):
    smallest = strings[1]
    longest = strings[0]

diff = len(longest) - len(smallest)

for char in range(len(smallest)):
    sums += ord(smallest[char]) * ord(longest[char])

if not diff == 0:
    longest = longest[-diff:]

    for el in range(len(longest)):
        sums += ord(longest[el])

print(sums)