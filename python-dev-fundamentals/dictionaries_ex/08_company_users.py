# COMPANY USERS

data = input()
users = {}

while not data == 'End':
    company, id = data.split(' -> ')

    if company not in users:
        users[company] = [id]
    else:
        if id in users[company]:
            pass
        else:users[company].append(id)

    data = input()

sorted_users = dict(sorted(users.items(), key=lambda x: x[0]))

for company,id in sorted_users.items():
    print(company)
    for id in sorted_users[company]:
        print(f'-- {id}')