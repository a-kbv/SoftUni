
lists = [el for el in input().split('|')]
new_l = []
for elem in lists:
    new_l.append([el for el in elem if el != " "])

while new_l:
    temp = new_l.pop()
    print(' '.join(temp), end=" ")

# 75/100