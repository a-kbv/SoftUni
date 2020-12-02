n = int(input())
users = {}

for user in range(n):
    command = input().split()
    if command[0] == 'register':
        user = command[1]
        license_Plate_Number = command[2]

        if user not in users:
            users[user] = license_Plate_Number
            print(f"{user} registered {license_Plate_Number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_Plate_Number}")

    if command[0] == 'unregister':
        user = command[1]
        if user in users:
            print(f"{user} unregistered successfully")
            del users[user]

        else:
            print(f"ERROR: user {user} not found")

for user in users:
    print(f"{user} => {users[user]}")