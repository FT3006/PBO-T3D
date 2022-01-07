class hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class hero")
        print("{} health: {}".format(
            self.name,
            self.health
            )
        )

class hero_intelligent(hero):
    def __init__(self,name):
        super().__init__(name, 100)

    def showInfo(self):
        print("showInfo di subclass hero_intelligent")
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
            self.name,
            self.health
            )
        )

class hero_strength(hero):
    def __init__(self,name):
        super().__init__(name, 200)

lina = hero_intelligent ('lina')
axe = hero_strength('axe')

lina.showInfo()