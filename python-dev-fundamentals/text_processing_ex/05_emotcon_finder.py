text = input()
[print(f":{text[i + 1]}") for i in range(len(text) - 1) if text[i] == ':']
