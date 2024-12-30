class coffee:
    def cost(self):
        return 5.0
    def description(self):
        return "plain coffee"
class coffeedecorator(coffee):
    def __init__(self,coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost()
    def description(self):
        return self.coffee.description()


class milk(coffeedecorator):
    def cost(self):
        return self.coffee.cost()+1.5
    def description(self):
        return self.coffee.description()+",Milk"

class sugar(coffeedecorator):
    def cost(self):
        return self.coffee.cost()+2
    def description(self):
        return self.coffee.description()+",Sugar"
    

class whipped_cream(coffeedecorator):
    def cost(self):
        return self.coffee.cost()+5
    def description(self):
        return self.coffee.description()+",Whipped cream"
    
if __name__ =="__main__":
    my_coffee=coffee()
    print(f"Description:{my_coffee.description()},Cost:{my_coffee.cost()}")

    
    my_coffee=milk(my_coffee)
    print(f"Description:{my_coffee.description()},Cost:{my_coffee.cost()}")

    
    my_coffee=sugar(my_coffee)
    print(f"Description:{my_coffee.description()},Cost:{my_coffee.cost()}")

    
    my_coffee=whipped_cream(my_coffee)
    print(f"Description:{my_coffee.description()},Cost:{my_coffee.cost()}")