class Hero :

    # class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # variable instance private 
        self.__private = "private"
        # variable instance protected
        self.__protected = "protected"

lina = Hero("lina",100)

print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah__)