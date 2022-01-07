class hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health: {}".format(self.name,self.health))

class hero_intelligent(hero):
    def __init__(self,name):
        super().__init__(name, 100)
        super().showInfo()

class hero_strength(hero):
    def __init__(self,name):
        super().__init__(name, 200)
        super().showInfo()

lina = hero_intelligent ('lina')
axe = hero_strength('axe')

