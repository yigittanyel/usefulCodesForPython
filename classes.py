class Player:
    def __init__(self,name,age,salary) :
        self.name=name
        self.age=age
        self.salary=salary

    def Yazdir(self):
        print(self.name+" "+str(self.age)+" "+str(self.salary))

p1=Player("Yigit",21,100)
p2=Player("Semih",30,140)

Player.Yazdir(p1)