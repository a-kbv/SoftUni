n_people = int(input())
lift = [int(el) for el in input().split(" ")]
max_seats_per_wagon = 4

for index in range(len(lift)):

    while not lift[index] == max_seats_per_wagon:

        if n_people > 0:
            lift[index] += 1
            n_people -= 1
        else:
            break

all_seats = len(lift) * max_seats_per_wagon
taken_seats = sum(lift)

if n_people == 0 and taken_seats < all_seats:
    print("The lift has empty spots!")
elif n_people > 0 and taken_seats == all_seats:
    print(f"There isn't enough space! {n_people} people in a queue!")

print(' '.join([str(el) for el in lift]))