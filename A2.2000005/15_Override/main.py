class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def showInfo(self):
        print("showinfo di class hero")
        print("{} health: {}".format(
            self.name,
            self.health
            )
        )


class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name,100)
        
        # Override
    def showInfo(self):
        print("showinfo di subclass Hero_intelligent")
        print("{} \n\t Tipe intelligent, \n\t health: {}".format(
            self.name,
            self.health
            )
        )    
        
        
class Hero_strenght(Hero):
    def __init__(self, name):
        super().__init__(name,200)
        
        
lina = Hero_intelligent('lina')
axe = Hero_strenght('axe')

lina.showInfo()   