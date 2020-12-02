usernames = input().split(', ')
valid_usernames = []
valid_symbols = ['-', '_']

for username in usernames:
    if 3 < len(username) < 16:

        if username.isalnum():
            valid_usernames.append(username)

        for sym in valid_symbols:
            if sym in username:
                valid_usernames.append(username)

print(f'\n'.join(valid_usernames))