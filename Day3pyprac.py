#prac1
x1,x2,x3,x4,x5 = 1,2,3,4,5
n = 5
avg = (x1 + x2 + x3 + x4 + x5)/ n
print("Avg is:", avg)
print("______________________________________________________________________________________________________________________")

# prac2
x = 24
if x % 2 == 0:
    print("No. is even")
else:
    print("No. is odd")
print("______________________________________________________________________________________________________________________")

#prac3
year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print(year ," is a leap year")  
       else:  
           print(year," is not a leap year")  
   else:  
       print(year ," is a leap year")  
else:  
   print(year, " is not a leap year")
print("______________________________________________________________________________________________________________________")

#prac4   
number = -5
if number == 0:
    print("Number  is zero")
elif number >= 0:
    print("Number is positive")
else:
    print("Number is negative")
print("______________________________________________________________________________________________________________________")

#prac5
x = 5
y = 10

if x == y: 
    print("Both are equal.")
elif x > y:
    print("x is greater.")
else:
    print("y is greater.")
print("______________________________________________________________________________________________________________________")

#prac6
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)    
print("______________________________________________________________________________________________________________________")

#prac7
a = 10
b = 20
print("before swap:", a)
print("before swap:", b)
temp = a
a = b
b = temp
print("After swap:", a)
print("After swap:", b)
print("______________________________________________________________________________________________________________________")

#prac8
p = 5
q = 10
if p < q:
    print(p , " is the smallest number")
else:
    print(q, " is smallest number")
print("______________________________________________________________________________________________________________________")

#prac9
num = 54
if num <= 100:
    if num % 2 ==0:
        print("it is even")
    else:
        print("it is odd")
else:
    print("Number is greater than 100")
print("______________________________________________________________________________________________________________________")

#prac10
no = 9
sq = no * no
if no <= 10:
    print("square of number is ", sq)
else:
    print("Number is bigger than 10.")
print("______________________________________________________________________________________________________________________")

#prac11
v = 50
if v >= 0:
    if v == 0:
        print("No is zero.")
    else:
        print("No is positive")
else:
    print("No is negative")
print("______________________________________________________________________________________________________________________")

#prac12
num1 = 10
num2 = 20
num3 = 5
if num1 > num2:
    if num1 > num3:
        print("greatest is: ", num1)
    else:
        print("greatest is ", num3)
if num2 > num1:
    if num2 > num3:
        print("greatest is: ", num2)
    else:
        print("greatest is ", num3)
else:
    print("greatest is: ", num3)
print("______________________________________________________________________________________________________________________")

#prac13
a1 = 2
a2 = 5
a3 = 6

if a1 < a2 and a2 < a3 :
    smallest = a1
elif a2 < a3 :
    smallest = a2
else :
    smallest = a3

print(smallest, "is the smallest of three numbers.")
print("______________________________________________________________________________________________________________________")

#prac14
x = 5
y = 7
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

x, y = y, x 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
print("______________________________________________________________________________________________________________________")

#prac15
no1 = int(input("Enter starting number: "))
no2 = int(input("Enter ending number: "))
for i in range(no1,no2 - 3,-3):
    print(i)
print("______________________________________________________________________________________________________________________")



