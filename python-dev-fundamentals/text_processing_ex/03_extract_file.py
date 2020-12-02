path = input().split('\\')
path = [el.split('.') for el in path if "." in el]
print(f"File name: {path[0][0]}")
print(f"File extension: {path[0][1]}")