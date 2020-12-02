food = (int(input()))*1000
food_eaten = 0

while True:
    adopted = input()
    if adopted == "Adopted":
        if food >= food_eaten:
            print(f"Food is enough! Leftovers: {food - food_eaten} grams.")
        else:
            print(f"Food is not enough. You need {food_eaten - food} grams more.")
        break
    food_eaten += int(adopted)
