class House:
    def __init__(self):
        self.address = None
        self.size = None
        self.material = None
        self.numBedrooms = None
        self.numBathrooms = None

    def __str__(self):
        return f"House at {self.address}, size: {self.size} sqft,material:{self.material}"

class WoodenHouse(House):
    def __init__(self):
        super().__init__()
        self.material = "wood"

class BrickHouse(House):
    def __init__(self):
        super().__init__()
        self.material = "brick"

class HouseBuilder:
    def __init__(self):
        self.house = None

    def create_house(self, house_type):
        if house_type == "wood":
            self.house = WoodenHouse()
        elif house_type == "brick":
            self.house = BrickHouse()
        else:
            raise ValueError("Invalid house type")

    def set_address(self, address):
        self.house.address = address

    def set_size(self, size):
        self.house.size = size

    def set_num_bedrooms(self, num_bedrooms):
        self.house.numBedrooms = num_bedrooms

    def set_num_bathrooms(self, num_bathrooms):
        self.house.numBathrooms = num_bathrooms

    def get_house(self):
        return self.house

builder = HouseBuilder()
builder.create_house("wood")
builder.set_address("123 Main St")
builder.set_size(2000)
builder.set_num_bedrooms(3)
builder.set_num_bathrooms(2)

wooden_house = builder.get_house()
print(wooden_house)

builder.create_house("brick")
builder.set_address("456 Elm St")
builder.set_size(2500)
builder.set_num_bedrooms(4)
builder.set_num_bathrooms(3)

brick_house = builder.get_house()
print(brick_house)