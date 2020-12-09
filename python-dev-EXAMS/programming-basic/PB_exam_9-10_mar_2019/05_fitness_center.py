
def fitnes():

    back = 0
    chest = 0
    legs = 0
    abs = 0
    protein_shake = 0
    protein_bar = 0

    visitors = int(input())
    for _ in range(visitors):
        ex = input()
        if ex == 'Back':
            back += 1
        elif ex == 'Chest':
            chest += 1
        elif ex == 'Legs':
            legs += 1
        elif ex == 'Abs':
            abs += 1
        elif ex == 'Protein shake':
            protein_shake += 1
        elif ex == 'Protein bar':
            protein_bar += 1

    work_out = ((back+ chest + legs + abs) / visitors) * 100
    protein = ((protein_shake + protein_bar) / visitors) * 100


    print(f"{back} - back")
    print(f"{chest} - chest")
    print(f"{legs} - legs")
    print(f"{abs} - abs")
    print(f"{protein_shake} - protein shake")
    print(f"{protein_bar} - protein bar")
    print(f"{work_out:.2f}% - work out")
    print(f"{protein:.2f}% - protein")



fitnes()