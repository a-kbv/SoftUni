text = input()
result = []
for i in range(len(text)-1):
    if not text[i] == text[i+1]:
        result.append(text[i])
result.append(text[-1])
print(''.join(result))
