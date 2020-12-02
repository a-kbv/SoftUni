
sizes = input()
colors = input()
count_stack = int(input())

stack_price = 0.0


color = ['Red', 'Green', 'Yellow']
size = ['Large', 'Medium', 'Small']

if colors == color[0]:
    if sizes == size[0]:
        print(f"{(16*count_stack*0.65):.2f} leva.")
    elif sizes == size[1]:
        print(f"{(13*count_stack*0.65):.2f} leva.")
    elif sizes == size[2]:
        print(f"{(9*count_stack*0.65):.2f} leva.")
elif colors == color[1]:
    if sizes == size[0]:
        print(f"{(12*count_stack*0.65):.2f} leva.")
    elif sizes == size[1]:
        print(f"{(9*count_stack*0.65):.2f} leva.")
    elif sizes == size[2]:
        print(f"{(8*count_stack*0.65):.2f} leva.")
elif colors == color[2]:
    if sizes == size[0]:
        print(f"{(9*count_stack*0.65):.2f} leva.")
    elif sizes == size[1]:
        print(f"{(7*count_stack*0.65):.2f} leva.")
    elif sizes == size[2]:
        print(f"{(5*count_stack*0.65):.2f} leva.")



