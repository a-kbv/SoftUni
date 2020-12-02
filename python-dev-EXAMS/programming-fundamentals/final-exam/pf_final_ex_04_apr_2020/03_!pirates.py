
def plunder(cities, data):
    # "Plunder=>{town}=>{people}=>{gold}"
    town, people, gold = data[1], int(data[2]), int(data[3])
    if town in cities:
        cities[town][0] -= people
        cities[town][1] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]

        return cities
    return cities

def prosper(cities, data):
    # "Prosper=>{town}=>{gold}"
    town,gold = data[1], int(data[2])
    if gold >= 0:
        cities[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
    else:
        print(f"Gold added cannot be a negative number!")
        return cities
    return cities


data = input()
cities = {}
while not data == 'Sail':
    city, citizen_count, gold = data.split('||')

    if city not in cities:
        cities[city] = [int(citizen_count),int(gold)]

    else:
        cities[city][0] += int(citizen_count)
        cities[city][1] += int(gold)
    data = input()

data = input()
while not data == 'End':
    data = data.split('=>')

    if data[0] == 'Plunder':
        cities = plunder(cities, data)
    if data[0] == 'Prosper':
        cities = prosper(cities, data)
    data = input()

if len(cities) > 0:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

"""
You could try the approach below, which sorts the dictionary by its items.
-item[1] sorts by value descending, while item[0] sorts by key ascending.
 Because the result of sorted is a list of tuples we need to convert it to a dict,
using the dict() constructor call.

if value is list you chose which element of the list to be used with -item[1][which.....]
"""
sorted_cities = dict(sorted(cities.items(), key=lambda item: (-item[1][1], item[0])))

for key,value in sorted_cities.items():
    print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')