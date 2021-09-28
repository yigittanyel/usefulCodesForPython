class Person:
    def __init__(self,fname,lname,age):
        self.fn=fname
        self.ln=lname
        self.age=age
    
    def print(self):
        print("Name: %s Surname: %s Age: %d" % (self.fn,self.ln,self.age))


class Student(Person):
    def __init__(self, fname, lname, age,gender):
        super().__init__(fname, lname, age)
        self.gen=gender

    def printS(self):
        print("Name: %s Surname: %s Age: %d Gender: %s" % (self.fn,self.ln,self.age,self.gen))
    



p1=Student("Yigit","Tanyel",21,"Male")
p2=Student("Bahar","XXX",25,"Female")
p1.printS()
p2.printS()