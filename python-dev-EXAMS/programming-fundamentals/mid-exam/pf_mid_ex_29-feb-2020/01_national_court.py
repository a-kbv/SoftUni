
emp_1, emp_2, emp_3, people_cnt = int(input()), int(input()), int(input()), int(input())
hours = 0
while people_cnt > 0:
    hours += 1
    if hours % 4 == 0:
        hours +=1
    people_cnt -= emp_1+emp_2+emp_3

print(f"Time needed: {hours}h.")