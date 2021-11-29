class Hero:

    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name   = inputName
        self.health = inputHealth
        self.power  = inputPower
        self.armor  = inputArmor
        Hero.jumlah += 1
        print("membuat hero dengan nama" + inputName)

hero1 = Hero("lesley", 100, 10, 4)
print(hero1.jumlah)
hero2 = Hero("alucard", 100, 15, 1)
print(hero1.jumlah)
hero3 = Hero("aldous", 1000, 100, 0)
print(hero1.jumlah)


