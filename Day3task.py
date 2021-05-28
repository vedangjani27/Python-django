#To take i/p from the user.
a = int(input("Enter number:"))
b = int(input("Enter number:"))
sum = a + b
print("sum is:" , sum)

x = 5
y = 10

if x == y: #we can also use if and if-else statment, but for multiple conditions we use if-elif-else statment.
    print("Both are equal.")
elif x > y:
    print("x is greater.")
else:
    print("y is greater.")

v = 50 #Nestes if
if v >= 0:
    if v == 0:
        print("No is zero.")
    else:
        print("No is positive")
else:
    print("No is negative")

i= 0 #While loop and break
while i <= 10:
    print(i)
    i += 1
    if i >= 5:
       break    

for i in "vedang": #For loop
    print("Value is:" , i)

list = ["Vedang", "Jani", 27] #Range() function
for i in list:
    print("o/p is:", i)

for m in range(1,11,2):
    print("Range is:" , m)

l2 = ["hello", "there", 2] #alt way and with else
for u in range(len(l2)):
    print(l2[u])
else:
    print("no further data")

for z in range(1,10): #continue statment
    if z % 2 == 0:
        continue
    print("odd numbers are:" , z)

p = {10,20,30} #pass is used when we have to keep the body empty.
for val in p:
    pass







