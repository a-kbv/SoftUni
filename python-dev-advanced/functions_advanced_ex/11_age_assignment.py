def age_assignment(*args, **kwargs):
    result_dict = {}

    for key in args:
        result_dict[key] = kwargs[key[0]]

    return result_dict

