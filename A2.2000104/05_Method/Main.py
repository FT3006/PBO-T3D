class Hero:
    # class variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputPower, inputHealth):
        #instance variabel
        self.name = inputName
        self.power = inputPower
        self.health = inputHealth
        Hero.jumlah_hero += 1

    # void function, method tanpa return
    def siapa(self):
        print("namaku adalah " + self.name)
        
    # method dengan argumen
    def healthUp(self,up):
        self.health += up
        
    # method dengan return
    def getHealth(self):
        return self.health
        
hero1 = Hero("sniper",10,100)
hero2 = Hero("mirana",15,100)

hero1.siapa()
hero1.healthUp(10)

print (hero1.getHealth())
