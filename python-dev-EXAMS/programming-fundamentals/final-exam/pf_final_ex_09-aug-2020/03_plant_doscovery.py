import re

class Plant:
    def __init__(self,name, rarity):
        self.name = name
        self.rarity = rarity
        self.ratings =[]

    def rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0


plants = {}
n = int(input())

for num in range(n):
    plant_name, plant_rarirty = input().split('<->')
    plants[plant_name] = Plant(plant_name,int(plant_rarirty))

data = input()
while not data == 'Exhibition':
    data_list = [(el) for el in re.split('[:\s]|[\s\-\s]', data) if not el == '']
    action = data_list[0]
    plant_name = data_list[1]
    if plant_name not in plants:
        print('error')
    elif action == 'Rate':
        rating = int(data_list[2])
        plants[plant_name].ratings.append(rating)
    elif action == 'Update':
        new_rarity = int(data_list[2])
        plants[plant_name].rarity = new_rarity
    elif action == 'Reset':
        plants[plant_name].ratings.clear()
    else:
        print('error')

    data = input()

sorted_plants = sorted(plants.values(), key=lambda p: (p.rarity, p.rating()), reverse=True)

print(f'Plants for the exhibition:')
for plant in sorted_plants:
    print(f'- {plant.name}; Rarity: {plant.rarity}; Rating: {plant.rating():.2f}')
