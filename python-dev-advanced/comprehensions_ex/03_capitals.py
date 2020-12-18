counry = input().split(', ')
capital = input().split(', ')

print('\n'.join([f"{k} -> {v}" for k, v in (dict(zip(counry, capital))).items()]))