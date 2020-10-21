#!/usr/bin/python3
#Nol Glamann
#05 November 2019

'''          circle.py 

program file that makes a circle with a cartesian 
graph point as the center
'''

import point as p
from math import pi

class Circle(object):
    
    def __init__(self, x=0, y=0, r=0):
        self.center = p.Point(x,y)
        self.radius = r
        
    def __str__(self):
        msg = ""
        msg += "Center: "+str(self.center)+" Radius: "+str(self.radius)
        return msg
    
    def diameter(self):
        return self.radius *2
    
    def circumference(self):
        return pi * self.diameter()
        
        
if __name__ == "__main__":
    circle1 = Circle(1,2,3)
    print(circle1)
    print("Diameter of Circle1: ", circle1.diameter())
    print("Circumference of Circle1: ", circle1.circumference())