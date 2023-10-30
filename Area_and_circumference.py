
#This program will calculate the area of a circumference of a circle
#import the math module to use the pi constant
import math
#Define a function to calculate the area of a circle
def calculate_area(radius):
    #area of a circle is pi * radius ^ 2 
    return math.pi * (radius **2)
#define a function to calculate the circumference of a circle
def calculate_circumference(radius):
    return 2 * math.pi * radius 
#get the radius from the user
radius = float(input("Enter the radius of the circle:"))  
#calculate area and circumference of the circle
area = calculate_area(radius)
circumference = calculate_circumference(radius)

#print the results
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")