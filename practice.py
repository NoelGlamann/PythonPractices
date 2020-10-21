#!usr/bin/python3
#Noel Glamann
#9/27/19 

""" Practice Problems;
      Teaching myself Python3"""


#Basic If Statement

#a = 25
#if(a == 5**2): print("I Did It!")
#print("Done")

#print()
#print()

# Complex If statement with 'elif's

#lname = input("Last Name: ")
#gen = input("Gender: ")

# Making input lower case
#gen = gen.lower()

#if gen == "female":
#    print("Ms.", lname)
#elif gen == "male":
#    print("Mr.", lname)
#else:
#    print("Mx.", lname)
#print("Done")

#print()
#print()

#Loops

#While::

#b = 3

#while b <= 17:
#    print(b)
#    b = b + 1
#print()

#For::

#c = list(range(6))

#for var in list(range(6)):
#    print("Hi")
#print("Done")

#Lists

y = input("my birth year: ")
m = input("my birth month: ")
d = input("my birth day: ")

mybday = [m, d, y]

y2 = input("sister's birth year: ")
m2 = input("sister's birth month: ")
d2 = input("sister's birth day: ")

sisbday = [m2, d2, y2]



print("My Birthday is", mybday[0] +"/"+  mybday[1] +"/"+  mybday[2])
print("My Sister's Birthday is", sisbday[0] +"/"+  sisbday[1] +"/"+  sisbday[2]) 

