class Hero:
    
    def __init__(self,name,health,power,armorNumber):
        self.name = name
        self.health = health
        self.power = power
        self.armorNumber = armorNumber
        
    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.power)
        
    def diserang(self, lawan, power_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = power_lawan/self.armorNumber
        print('serangan terasa : ' + str(attack_diterima))
        self.health = attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))
      
sniper = Hero('sniper',100,10,5)
mirana = Hero('mirana',100,20,10)

sniper.serang(mirana)
print("\n")
mirana.serang(sniper)
print("\n")
