<<<<<<< HEAD
class Hero:
    
    # private class variabel
    __jumlah = 0;
    
    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1
        
    def getJumlah(self):
        return Hero.__jumlah

    def getJumlah(self):
        return Hero.__jumlah
        
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
        
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
        
sniper = Hero('snper')
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drowranger = Hero('drowranger')
print(Hero.getJumlah3())
=======
class Hero:
    
    # private class variabel
    __jumlah = 0;
    
    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1
        
    def getJumlah(self):
        return Hero.__jumlah

    def getJumlah(self):
        return Hero.__jumlah
        
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
        
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
        
sniper = Hero('snper')
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drowranger = Hero('drowranger')
print(Hero.getJumlah3())
>>>>>>> a1ce7e788580d8a96849a347ea6fa79fe930bf4f
