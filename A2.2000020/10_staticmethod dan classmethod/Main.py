class Hero:

    #private class variabel
    __jumlah = 0;

    def _init_(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getjumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getjumlah1():
        return Hero.__jumlah
    
    # method static (decorator) nempel ke objek dan class nya 
    @staticmethod 
    def getjumlah2():
        return Hero.__jumlah

    @classmethod
    def getjumlah3(cls):
        return cls.__jumlah



sniper = Hero('sniper')
print(Hero.getjumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getjumlah2())
drowranger= Hero('drowranger')
print(Hero.getjumlah3())