class BankAccount:
    def __init__(self,name,money,address):
        self.name=name
        self.__money=money
        self.adress=address

    def getMoney(self):
        return self.__money
    def setMoney(self,amount):
        self.__money=amount


p1=BankAccount("Yigit",2500,"Bursa")
p2=BankAccount("Semih",3460,"İstanbul")

print("Money of Yigit: %d" %(p1.getMoney()))
p2.setMoney(3500)
print("Money of Semih: {0}".format(p2.getMoney()))