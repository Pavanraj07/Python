from abc import ABC, abstractmethod

# Abstract Product classes
class SportEquipment(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class Apparel(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

# Concrete Product classes for Running
class RunningShoes(SportEquipment):
    def get_name(self):
        return "Decathlon Running Shoes"

    def get_price(self):
        return 50.0

class RunningTShirt(Apparel):
    def get_name(self):
        return "Decathlon Running T-Shirt"

    def get_price(self):
        return 20.0

# Concrete Product classes for Cycling
class CyclingHelmet(SportEquipment):
    def get_name(self):
        return "Decathlon Cycling Helmet"

    def get_price(self):
        return 30.0

class CyclingGloves(Apparel):
    def get_name(self):
        return "Decathlon Cycling Gloves"

    def get_price(self):
        return 15.0

# Abstract Factory class
class DecathlonFactory(ABC):
    @abstractmethod
    def create_sport_equipment(self):
        pass

    @abstractmethod
    def create_apparel(self):
        pass

# Concrete Factory classes
class RunningFactory(DecathlonFactory):
    def create_sport_equipment(self):
        return RunningShoes()

    def create_apparel(self):
        return RunningTShirt()

class CyclingFactory(DecathlonFactory):
    def create_sport_equipment(self):
        return CyclingHelmet()

    def create_apparel(self):
        return CyclingGloves()

# Client code
def create_decathlon_products(factory: DecathlonFactory):
    equipment = factory.create_sport_equipment()
    apparel = factory.create_apparel()

    print(f"Equipment: {equipment.get_name()}, Price: ${equipment.get_price()}")
    print(f"Apparel: {apparel.get_name()}, Price: ${apparel.get_price()}")

running_factory = RunningFactory()
cycling_factory = CyclingFactory()

print("Running Products:")
create_decathlon_products(running_factory)

print("\nCycling Products:")
create_decathlon_products(cycling_factory)
