class Employee:
    def raisee(self):
        raise_rate=0.1
        result=100 + 100*raise_rate
        print("Standart Employee: %d" %result)

class CompEng(Employee):
    def raisee(self):
        raise_rate=0.3
        result=100 +100*raise_rate
        print("Computer Engineer: %d " %result)

class MacEng(Employee):
    def raisee(self):
        raise_rate=0.2
        result=100 +100*raise_rate
        print("Machine Engineer: %d " %result)

e1=Employee()
ce=CompEng()
me=MacEng()

employee_list=[e1,ce,me]
for emp in employee_list:
    emp.raisee()