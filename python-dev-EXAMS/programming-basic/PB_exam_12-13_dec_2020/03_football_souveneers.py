def souveneers():
    country = input()
    souveneer = input()
    bought_souveneer = int(input())
    price = 0
    country_t = "Argentina", "Brazil", "Croatia", "Denmark"
    souveneer_t = "flags", "caps", "posters", "stickers"

    if country == 'Argentina':
        if souveneer == 'flags':
            price = 3.25
        elif souveneer == "caps":
            price = 7.20
        elif souveneer == "posters":
            price = 5.10
        elif souveneer == "stickers":
            price = 1.25

    elif country == 'Brazil':
        if souveneer == 'flags':
            price = 4.20
        elif souveneer == "caps":
            price = 8.50
        elif souveneer == "posters":
            price = 5.35
        elif souveneer == "stickers":
            price = 1.20

    elif country == 'Croatia':
        if souveneer == 'flags':
            price = 2.75
        elif souveneer == "caps":
            price = 6.90
        elif souveneer == "posters":
            price = 4.95
        elif souveneer == "stickers":
            price = 1.10

    elif country == 'Denmark':
        if souveneer == 'flags':
            price = 3.10
        elif souveneer == "caps":
            price = 6.50
        elif souveneer == "posters":
            price = 4.80
        elif souveneer == "stickers":
            price = 0.90

    if country in country_t and souveneer in souveneer_t:
        return f'Pepi bought {bought_souveneer} {souveneer} of {country} for {(bought_souveneer * price):.2f} lv.'
    elif country in country_t and souveneer not in souveneer_t:
        return "Invalid stock!"
    elif country not in country_t and souveneer in souveneer_t:
        return "Invalid country!"


print(souveneers())