words = {word:len(word) for word in input().split(', ')}
print(', '.join([f"{k} -> {v}" for k,v in words.items()]))
