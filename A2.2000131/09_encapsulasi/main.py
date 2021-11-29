class Hero:
    def __init__(self ,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

        #getter
        def getname(self):
            return self.__name

        def gethealth(self):
            return self.__health

        #setter
        def diserang(self,serangPower):
            self.__ -= serangPower

        def setAttPower(self,nilaibaru):
            self.__attPower = nilaibaru

#awal dari game
earthshaker = Hero("earthshaker",50,5)

#game berjalan

print(earthshaker.getname())
print(earthshaker.gethealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())