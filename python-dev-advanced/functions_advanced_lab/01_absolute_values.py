def to_abs_list(values):
    return [abs(float(x)) for x in values]

print(to_abs_list(input().split()))