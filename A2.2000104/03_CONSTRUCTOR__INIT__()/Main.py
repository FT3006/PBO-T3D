class Hero: # template

    def __init__(self, inputName, inputPower, inputHealth):
        self.name = inputName
        self.power = inputPower
        self.health = inputHealth


hero1 = Hero("sniper",10,100)
hero2 = Hero("mirana",15,100)

print(hero1.__dict__)
print(hero2.__dict__)
