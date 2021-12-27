class hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

class hero_intelligent(hero):
    pass

class hero_strength(hero):
    pass

lina = hero ('lina',100)
techies = hero_intelligent('techies',50)
axe = hero_strength('axe',200)

print(lina.name)
print(techies.name)
print(axe.name)