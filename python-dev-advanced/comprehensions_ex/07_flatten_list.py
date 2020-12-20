# ex input : 1 2 3 |4 5 6 |  7  8

print(' '.join(el for x in input().split('|')[::-1] for el in x.split()))

