class hero: #template
    #class variable
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputpower, inputArmor) :
    
        self.name = inputName
        self.health = inputHealth
        self.power = inputpower
        self.armor = inputArmor
        hero.jumlah += 1
        print("membuat hero dengan nama" + inputName)
        

hero1 = hero("sniper",100,10,4)
print(hero.jumlah)
hero2 = hero("mirana",200,15,1)
print(hero.jumlah)
hero3 = hero("ucup",100,100,0)
print(hero.jumlah)