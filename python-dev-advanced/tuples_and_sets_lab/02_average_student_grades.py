


def add_students(n, student_dict):
    for _ in range(n):
        data = input().split(' ')
        student, grade = data
        if student not in student_dict:
            student_dict[student] = [float(grade)]
        else:
            student_dict[student].append(float(grade))
    return student_dict

def avg(grade):

    return sum(grade) / len(grade)

def print_result(student_dict):
    for key, value in student_dict.items():
        print(f"{key} -> {f' '.join(f'{mark:.2f}' for mark in value)} (avg: {avg(value):.2f})")

def average_students_grade():
    n = int(input())
    student_dict = {}
    student_dict = add_students(n, student_dict)
    print_result(student_dict)

average_students_grade()
