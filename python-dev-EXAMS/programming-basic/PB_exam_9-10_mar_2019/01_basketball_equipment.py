tax = int(input())

trousers = tax * 0.6
jacket = trousers * 0.8
ball = jacket * 0.25
accesory = ball * 0.2

print(f"{(trousers+jacket+ball+accesory+tax):.2f}")