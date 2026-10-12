class employee:
    #salary=890
    #name="rohan"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
  
    def getsalary(self):
        #return self.salary
        print(self.salary)

rohan=employee("rohan","54000")
#print(rohan.salary)
#print(rohan.name)
rohan.getsalary()


ritesh=employee("ritesh","45000")
#print(ritesh.salary)
#rint(ritesh.name)
ritesh.getsalary()

