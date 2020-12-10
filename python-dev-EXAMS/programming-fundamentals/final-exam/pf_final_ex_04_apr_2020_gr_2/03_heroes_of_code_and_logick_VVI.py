# def cast_spell(heroes_dict, hero_name, mp_needed, spell_name):
#     if heroes_dict[hero_name][1] > mp_needed:
#         heroes_dict[hero_name][1] -= mp_needed
#         print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")
#     else:
#         print(f"{hero_name} does not have enough MP to cast {spell_name}!")
#     return heroes_dict
#
# def take_damage(heroes_dict, hero_name, damage, attacker):
#     heroes_dict[hero_name][0] -= damage
#     if heroes_dict[hero_name][0] > 0:
#         print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!")
#     else:
#         del heroes_dict[hero_name]
#         print(f"{hero_name} has been killed by {attacker}!")
#     return heroes_dict
#
# def recharge(heroes_dict, hero_name, amount):
#     max = 200
#     if heroes_dict[hero_name][1] + amount > max:
#         amount -= ((heroes_dict[hero_name][1] + amount) - max)
#         heroes_dict[hero_name][1] = max
#     else:
#         heroes_dict[hero_name][1] += amount
#     print(f"{hero_name} recharged for {amount} MP!")
#     return heroes_dict
#
# def heal(heroes_dict, hero_name, amount):
#     max = 100
#     if heroes_dict[hero_name][0] + amount > max:
#         amount -= ((heroes_dict[hero_name][0] + amount) -max)
#         heroes_dict[hero_name][0] = max
#     else:
#         heroes_dict[hero_name][0] += amount
#
#     print(f"{hero_name} healed for {amount} HP!")
#     return heroes_dict
#
# def play():
#     heroes_dict = {}
#     n = int(input())
#     for _ in range(n):
#         data = input().split(' ')
#         hero_name, hp, mp = data[0], int(data[1]), int(data[2])
#         heroes_dict[hero_name] = [hp, mp]
#
#     data = input()
#     while not data == 'End':
#         data = data.split(' - ')
#         command = data[0]
#         hero_name = data[1]
#         value = int(data[2])
#
#         if command == "CastSpell":
#             spell_name = data[3]
#             heroes_dict = cast_spell(heroes_dict, hero_name, value, spell_name)
#
#         elif command == "TakeDamage":
#             attacker = data[3]
#             heroes_dict = take_damage(heroes_dict, hero_name, value, attacker)
#
#         elif command == "Recharge":
#             heroes_dict = recharge(heroes_dict, hero_name, value)
#
#         elif command == "Heal":
#             heroes_dict = heal(heroes_dict, hero_name, value)
#
#         data = input()
#
#     sorted_heroes = sorted(heroes_dict.items(), key=lambda x: (-x[1][0], x[0]))
#     for name, value in sorted_heroes:
#         print(name)
#         print(f"  HP: {value[0]}")
#         print(f"  MP: {value[1]}")
# play()

def cast_spell(heroes_dict, hero_name, mp_needed, spell_name):
	current_mana_points = heroes_dict[hero_name]['MP']
	if mp_needed > current_mana_points:
		print(f"{hero_name} does not have enough MP to cast {spell_name}!")
	else:
		heroes_dict[hero_name]['MP'] = (current_mana_points - mp_needed)
		print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['MP']} MP!")
	return heroes_dict


def take_damage(heroes_dict, hero_name, damage, attacker):
	current_health_points = heroes_dict[hero_name]['HP']
	healths_point_left = current_health_points - damage
	if healths_point_left <= 0:
		del heroes_dict[hero_name]
		print(f"{hero_name} has been killed by {attacker}!")
	else:
		heroes_dict[hero_name]['HP'] = healths_point_left
		print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {healths_point_left} HP left!")
	return heroes_dict


def recharge(heroes_dict, hero_name, amount):
	current_mana_points = heroes_dict[hero_name]["MP"]
	if current_mana_points + amount >= 200:
		heroes_dict[hero_name]["MP"] = 200
		print(f"{hero_name} recharged for {200 - current_mana_points} MP!")
	else:
		heroes_dict[hero_name]["MP"] += amount
		print(f"{hero_name} recharged for {amount} MP!")
	return heroes_dict


def heal(heroes_dict, hero_name, amount):
	current_mana_points = heroes_dict[hero_name]["HP"]
	if current_mana_points + amount >= 100:
		heroes_dict[hero_name]["HP"] = 100
		print(f"{hero_name} healed for {100 - current_mana_points} HP!")
	else:
		heroes_dict[hero_name]["HP"] += amount
		print(f"{hero_name} healed for {amount} HP!")
	return heroes_dict


heroes = {}

n = int(input())

for _ in range(n):
	data = input().split(' ')
	name = data[0]
	hit_points = int(data[1])
	mana_points = int(data[2])
	heroes[name] = {"HP": hit_points, "MP": mana_points}

command_data = input()

while not command_data == "End":
	command_data = command_data.split(" - ")
	command = command_data[0]

	if command == "CastSpell":
		hero_name = command_data[1]
		mp_needed = int(command_data[2])
		spell_name = command_data[3]
		heroes = cast_spell(heroes, hero_name, mp_needed, spell_name)

	elif command == "TakeDamage":
		hero_name, damage, attacker = command_data[1:]
		damage = int(damage)
		heroes = take_damage(heroes, hero_name, damage, attacker)

	elif command == "Recharge":
		hero_name = command_data[1]
		amount = int(command_data[2])
		heroes = recharge(heroes, hero_name, amount)

	elif command == "Heal":
		hero_name = command_data[1]
		amount = int(command_data[2])
		heroes = heal(heroes, hero_name, amount)
	command_data = input()

sorted_heroes = sorted(heroes.items(), key=lambda x: (-x[1]['HP'], x[0]))

for name, value in sorted_heroes:
	print(name)
	print(f"  HP: {value['HP']}")
	print(f"  MP: {value['MP']}")