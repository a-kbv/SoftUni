data =input()
courses = {}

while not data == "end":
    course, employee = data.split(' : ')

    if not course in courses:
        courses[course] = [employee]
    else:
        if employee in courses[course]:
            pass
        else:
            courses[course].append(employee)
    data = input()

# sort courses by lenght
sorted_courses = dict(sorted(courses.items(), key=lambda x: (len(x[1])), reverse=True))

# sort emplyees alphabetically
for course, employee in sorted_courses.items():
    sorted_courses[course] = employee.sort()


for course, employee in sorted_courses.items():
    print(f'{course}: {len(courses[course])}')
    for employee in courses[course]:
        print(f'-- {employee}')
