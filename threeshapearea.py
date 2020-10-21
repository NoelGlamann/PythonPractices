#!/usr/bin/python3
# Noël Glamann
# August 29, 2019

# This program computes the area of a rectangle, circle, or triangle after being given length and width by the user.

#welcoming statement
print(" ")
print("           Let's calculate the area!")
print("           -------------------------")


print("Welcome to the area program!\n\n")

print("This calculator can find the area of three different shapes.\n")

print("1. Rectangle")
print("2. Circle")
print("3. Triangle\n")

#have the user choose what shape they want to find the area of
print("What shape would you like?")
shape = input("Number: ")



#length <-  input
print(" ")
L = input("What is the length? ")
L = float(L)

#width <-  input
print(" ")
W = input("What is the width? ")
W = float(W)

#area <-  length * width
A = L * W

#display area
print(" ")
print("The area is:", A)


