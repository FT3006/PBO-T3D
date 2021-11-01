class Hero:
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self)

    def diserang(self, lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = lawan.attack/self.armor
        print('serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))

sniper = Hero('sniper', 100, 10, 5)
rikimaru = Hero('rikimaru', 100, 20, 10)

sniper.serang(rikimaru)
print('\n')
rikimaru.serang(sniper)
print('\n')
rikimaru.serang(sniper)
print('\n')
rikimaru.serang(sniper)
print('\n')
rikimaru.serang(sniper) 
