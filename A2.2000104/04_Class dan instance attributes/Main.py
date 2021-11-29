<<<<<<< HEAD
class Hero: # template
    #class variabel
    jumlah = 0
    
    def __init__(self, inputName, inputPower, inputHealth):
        # instance variabel
        self.name = inputName
        self.power = inputPower
        self.health = inputHealth
        Hero.jumlah += 1
        print("Membuat Hero dengan nama " + inputName)


hero1 = Hero("sniper",10,100)
print(Hero.jumlah)
hero2 = Hero("mirana",15,100)
print(Hero.jumlah)
=======
class Hero: # template
    #class variabel
    jumlah = 0
    
    def __init__(self, inputName, inputPower, inputHealth):
        # instance variabel
        self.name = inputName
        self.power = inputPower
        self.health = inputHealth
        Hero.jumlah += 1
        print("Membuat Hero dengan nama " + inputName)


hero1 = Hero("sniper",10,100)
print(Hero.jumlah)
hero2 = Hero("mirana",15,100)
print(Hero.jumlah)
>>>>>>> c3bb575a669627f5222be438b869b71bee68f224
