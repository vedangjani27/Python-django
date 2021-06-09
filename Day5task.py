#prac 1
class cal1:
    n1 = 0
    n2 = 0
    n3 = 0
    
    def setdata(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def display(self):
        sum = self.n1 + self.n2 + self.n3
        print("sum is:", sum)

myo = cal1()
myo.setdata(10,20,30)
myo.display()

# prac 2
class cal2:
    r = 0
    area = 0

    def setdata(self):
        r = int(input("Enter radius: "))
        self.r = r
    def area(self):
        area = (3.14 * (self.r ** 2))
        self.area = area
    def display2(self):
        print("area is ", self.area)

myo1 = cal2()
myo1.setdata()
myo1.area()
myo1.display2()

# prac 3
class cal3:
    p = 0
    n = 0
    r = 0
    SI = 0

    def __init__(self,p,n,r):
        self.p = p
        self.n = n
        self.r = r
    def callInterest(self):
        SI = ((self.p * self.n * self.r)/100)
        self.SI = SI
    def display3(self):
        print("Simple Interest is ", self.SI)

myo1 = cal3(1000,1,2)
myo1.callIntrest()
myo1.display3()

# prac 4
class cal4:
    a = 0

    def setdata(self,a):
        self.a = a
    def display4(self):
        square = self.a ** 2
        return square #method returns value.

myobj = cal4()
myobj.setdata(5)
print(myobj.display4())

# prac 5
class employee():
    
    def ename(self):
        print("It contains name field.")
        print("It contains desgination field.")

class subemployee(employee):

    def empSalary(self):
        print("It contains salary field.")

c = subemployee()
c.empSalary()
c.ename()

#prac 6
class cal5():
    l=0
    w=0
    a=0

    def __init__(self,length,width):
        self.l=length
        self.w=width
    
    def calArea(self):
        self.a = self.l * self.w

    def display6(self):
        print('The area of Rectangle is :',self.a)

c6= cal5(10,20)
c6.calArea()
c6.display6()

#prac 7
class cal6():
    length=0
    area=0


    def setdata7(self):
        self.length= int(input("Enter the length: "))

    def area7(self):
        self.area = self.length ** 2
    
    def display7(self):
        print('The are of a Square is :', self.area)

c7= cal6()
c7.setdata7()
c7.area7()
c7.display7()

#prac 8
class publisher():
    t=''

    def title(self):
        self.t= input('Enter the name of the Title :')

class book(publisher):
    pgnum=''

    def page(self):
        self.pgnum= int(input('Enter the page number :'))

    def display8(self):
        print('The title name is :',self.t)
        print('The page number is :',self.pgnum)

class tape(publisher):
    time=''
    def timeplay(self):
        self.time= int(input('Enter time for playing :'))

    def display8(self):
        print('The time for playing is :',self.time)


cla=book()
cla.title()
cla.page()
clb=tape()
clb.timeplay()
cla.display8()
clb.display8()

#prac 9
class scheme():
    schid=7070
    schname='unlimited call'
    outgoingrate=700
    messagecharge=5

class customer(scheme):
    custid= 2701
    name='Vedang Jani'
    mobileno=9876543210

    def detail(self):
        print('customer name :',self.name)
        print('customer id :',self.custid)
        print('customer mobile number :',self.mobileno)
        print('scheme id :',self.schid)
        print('scheme name :',self.schname)
        print('scheme outgoing rate :',self.outgoingrate)
        print('scheme message rate :',self.messagecharge)
      
c9=customer()
c9.detail()

#prac 10 
class arith():
    n1=''
    n2=''

    def __init__(self,num1,num2):
        self.n1=num1
        self.n2=num2

    def cal10(self):
        add= self.n1 + self.n2
        sub= self.n1 - self.n2
        multi=self.n1 * self.n2

        print('addition is :',add)
        print('subtraction is :',sub)
        print('multiplication is :',multi)
        
c10=arith(10,5)
c10.cal10()



