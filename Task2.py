""" this is a 
multi line cmmt"""

'''this too is 
a multi line
cmmt.'''

a = "Hello, there"
b = 10.5
c = 20
print( a + " is a string." )
print(b)
print(c, " is a int value. ")

c = d = e = 10 
user,number,role = "abc123", 5, "coder" 
print(c)
print(d)
print("userid is:", user)
print(number , role)

n1 = 50.7
print(type(n1))

n2 = 10+2j
print(isinstance(n2, complex))

webTech = " Python django"
print(webTech[2])
print(webTech[2:6])
print(webTech[2:])
print(webTech[:5])
print(webTech * 2)

list1 = ["python", "django", 7, 7.5]
print(list1)
print(list1[1:3])
print("languages list are as: ", list1[0:2])
print(type(list1))
list1[1] = "java"
print(list1)

tuple1 = ("java", "js", 10 , 10.5 , 7)
print(tuple1)
print(type(tuple1))
print(tuple1[2])
# here tupple can not be modified later as list as it brings an error.

dic = {1: "python", 2: "java", "key": 5} #here values are assigned using ([]) braces in dictionary.
print(dic)
print("D[2]: ", dic[2])
print(dic[1])
print("vakue of key  is: ", dic["key"])


