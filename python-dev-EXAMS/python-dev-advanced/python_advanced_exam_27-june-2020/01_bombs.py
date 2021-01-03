
def check_for_match(sum_bomb, bomb_dict):
    for key, value in bomb_dict.items():
        if sum_bomb == value:
            pouch[key] = value
            del bomb_effects[0]
            del bomb_casing[-1]

        else:
            if bomb_casing:
                bomb_casing[-1] -= 5
                break

def make_bombs(bomb_effects, bomb_casing, bomb_dict, pouch):
    sum_bomb = bomb_effects[0] + bomb_casing[-1]
    for key, value in bomb_dict.items():
        if sum_bomb == value:
            pouch[key] += 1
            del bomb_effects[0]
            del bomb_casing[-1]
            return pouch
    bomb_casing[-1] -= 5
    return pouch


if __name__ == "__main__":

    pouch = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

    bomb_effects = [int(el) for el in input().split(", ")]
    bomb_casing = [int(el) for el in input().split(", ")]
    bomb_dict = {"Datura Bombs": 40, "Cherry Bombs": 60, "Smoke Decoy Bombs": 120}

    while True:
        if bomb_effects and bomb_casing and not all(value >= 3 for value in pouch.values()):
            pouch = make_bombs(bomb_effects, bomb_casing, bomb_dict, pouch)
        else:
            break

    if not all(value >= 3 for value in pouch.values()):
        print(f"You don't have enough materials to fill the bomb pouch.")
    else:
        print(f"Bene! You have successfully filled the bomb pouch!")
    if bomb_effects:
        print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
    else:
        print("Bomb Effects: empty")
    if bomb_casing:
        print(f"Bomb Casings: {', '.join(map(str, bomb_casing))}")
    else:
        print("Bomb Casings: empty")
    print(f"Cherry Bombs: {pouch['Cherry Bombs']}")
    print(f"Datura Bombs: {pouch['Datura Bombs']}")
    print(f"Smoke Decoy Bombs: {pouch['Smoke Decoy Bombs']}")
