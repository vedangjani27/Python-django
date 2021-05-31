def func (name):
    print("My name is:", name)
func("Vedang Jani")
print("************************************************************************************************************************")

# deining func with return keyword
def func2():
    myname = "Vedang Jani"
    contact = 987654321
    return myname,contact
myname,contact = func2()
print("name is:", myname)
print("contact is:", contact)
print(func2())
print("************************************************************************************************************************")

#using default arg.
def f1(a=10, b = 20):
    print(a+b)
f1(15,5)#with arg
f1()#without arg

#using keyword arg
def f2(a, b):
    print(a+b)
f2(b = 15,a =5)

#using variable length arg
def f3(*num):  # '*' is used for non-keyword var-length arg and '**' for keyword var-length arg.
    sum = 0

    for n in num:
        sum = sum + n
        print("sum is: ", sum)
        
f3(10,20)
f3(10,25,5)

def my_name(**arg): #keyword arg.
    for i, j in arg.items():
        print(i,j)
my_name(Name = 'Vedang', Lastname = 'Jani')
print("************************************************************************************************************************")

#global and local var.
def hello():
    x = 10 #local var(inside the func.)
    print("local variable is: ", x)

x = 20 #global var
hello()
print("global variable is: ", x)
print("************************************************************************************************************************")

#import module
import scratch                      #here a module is imported and then it's code is executed.
print(scratch.fun2("Vedang Jani"))    
print("************************************************************************************************************************")

#Operations in python
u = 10
v = 2
print("u + v:", u + v ) #add
print("u - v:", u - v ) #sub
print("u * v:", u * v ) #mult
print("u / v:", u / v ) #div
print("u // v:", u // v ) #floor division
print("u ** v:", u ** v ) #Exponent
print("u % v:", u % v ) #modulus
print("************************************************************************************************************************")

#comparison operators
print(u > v)
print(u < v)
print(u == v)
print(u != v)
print(u >= v)
print(u >= v)

#and operator
a1 = 10 
a2 = 20 
a3 = 15
if(a1 > a2 and a1 > a3):
    print("a1 is largest")
if(a2 > a1 and a2 > a3):
    print("a2 is largest") 
else:
    print("a3 is largest") 

# or operator     
ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")
print("************************************************************************************************************************")

#membership operators
x1 = 10
x2 = 5
l1 = [10,15,40,30]

print(x1 in l1) #in operator
print(x2 in l1) 
print(x2 not in l1) #not in op

#Identity op
p = 10
q = 20
print(p is q) #is op.
print(p is not q) #is not opt.