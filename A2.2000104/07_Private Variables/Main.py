<<<<<<< HEAD
class Hero:
    
    # class variabel
    jumlah = 0
    __privateJumlah = 0
    
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
        # variabel instance private
        self.__private = "private"
        # variabel instance protected
        self._protected = "protected"
        
        
Lina = Hero("Lina",100)

print(Lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)
=======
class Hero:
    
    # class variabel
    jumlah = 0
    __privateJumlah = 0
    
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
        # variabel instance private
        self.__private = "private"
        # variabel instance protected
        self._protected = "protected"
        
        
Lina = Hero("Lina",100)

print(Lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)

>>>>>>> 2c5da10c182efdf364fc409511d14bfb39056399
