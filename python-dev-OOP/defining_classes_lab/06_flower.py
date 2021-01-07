class Flower:
    is_happy = False

    def __init__(self, name, req_water):
        self.name = name
        self.req_water = req_water
        self.water_1 = 0

    def water(self, water_to_add):
        self.water_1 += water_to_add
        if self.water_1 >= self.req_water:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
