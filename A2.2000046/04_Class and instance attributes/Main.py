class jawaraSumedang:
 #class variable
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        jawaraSumedang.jumlah += 1
        print("Membuat jawara dengan nama " + inputName)

jawaraPertama = jawaraSumedang("Dede", 100, 78, 80)
print(jawaraSumedang.jumlah)
jawaraKedua   = jawaraSumedang("Sugih", 100, 90, 20)
print(jawaraSumedang.jumlah)
jawaraKetiga  = jawaraSumedang("Ivan", 150, 75, 78)
print(jawaraSumedang.jumlah)