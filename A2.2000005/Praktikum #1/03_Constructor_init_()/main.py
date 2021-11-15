class hero: #template
    def __init__(self, inputName, inputHealth, inputpower, inputArmor) :
    
        self.name = inputName
        self.health = inputHealth
        self.power = inputpower
        self.armor = inputArmor
        

hero1 = hero("sniper",100,10,4)
hero2 = hero("mirana",200,15,1)
hero3 = hero("ucup",100,100,0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)