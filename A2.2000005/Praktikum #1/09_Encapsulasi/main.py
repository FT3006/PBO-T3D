class hero:
    
    def __init__(self,name,health,attackpower):
        self.__name = name
        self.__health = health
        self.__attpower = attackpower
        
    # getter
    def getname(self):
            return self.__name
        
    def gethealth(self):
            return self.__health
        
    # setter

    def diserang(self,serangPower):
        self.__health -= serangPower

    def setAttPower(self,nilaibaru):
        self.__attPower = nilaibaru

# awal dari game
earthshaker= hero ("earthshaker", 50, 5)

# game berjalan

print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())