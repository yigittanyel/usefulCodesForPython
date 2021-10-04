class Website:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

    def login(self):
        print("Welcome "+self.name+" "+self.surname)

class Webssite1(Website):
    def __init__(self, name, surname,id):
        super().__init__(name, surname,)
        self.id=id
    
    def login1(self):
        print("Welcome "+self.name +" "+self.surname +" "+ str(self.id))
    
class Website2(Website):
    def __init__(self, name, surname,email):
        super().__init__(name, surname)
        self.email=email
    
    def login2(self):
         print("Welcome "+self.name +" "+self.surname +" "+ self.email)


w1=Website("Yigit","Tanyel")
w2=Webssite1("Semih","Tanyel",7)
w3=Website2("Yusuf","Tanyel","abc@gmail.com")

w1.login()
w2.login1()
w3.login2()