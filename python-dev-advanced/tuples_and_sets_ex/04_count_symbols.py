def occurances_in_string(text=input()):
    char_dict = {}

    for el in text:
        if el not in char_dict:
            char_dict[el] = 1
        else:
            char_dict[el] += 1

    for k, v in sorted(char_dict.items(), key=lambda x: x[0]):
        print(f"{k}: {v} time/s")

occurances_in_string()
