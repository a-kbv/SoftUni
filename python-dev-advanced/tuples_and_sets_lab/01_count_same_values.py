
def count_numbers(tupl, t_dict):
    for el in tupl:
        if el not in t_dict:
            t_dict[el] = 1
        else:
            t_dict[el] += 1
    return t_dict

def occurences():
    tupl = (float(el) for el in input().split())
    t_dict = {}
    count_numbers(tupl, t_dict)
    for key, value in t_dict.items():
        print(f"{key} - {value} times")

occurences()