age=25
height=1.7
complex_number=3+6j
#calculating area of a triangle
b=input("Enter the of base of the triangle as:")
h=input("Enter the height of the triangle as:")
area=(0.5)*int(b)*int(h)
area=int(area)
print("The area of a triangle is",area)
#calculating the perimeter of a triangle
a=input("Enter the first side as a:")
b=input("Enter the second side as b:")
c=input("Enter the third side as c:")
perimeter=int(a)+int(b)+int(c)
print("The perimeter of a triangle is",perimeter)
#calculating area and perimeter using prompt
length=input("Enter the length of a rectangle:")
width=input("Enter the width of a rectangle:")
area=int(length)*int(width)
perimeter=2*(int(length)+int(width))
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:",perimeter)
#calculating the area of a circle
from math import pi
r=input("Enter the radius of the circle:")
area=pi*int(r)*int(r)
circumference=2*pi*int(r)
print("The area of the circle is:",area)
print("The circumference of the circle is:",circumference)
#finding the slope and intercept of two point 
def slope(x1, y1, x2, y2):
  m = (y2-y1)/(x2-x1)
  return m

print(slope(2,2,6,10))
#Quadratic formular. 
print("The general quadratic solution of the form x^2+6x+9")
import cmath
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter  the value of c:"))
d=(b**2)-(4*a*c)
y1=(-b+cmath.sqrt(d))/(2*a)
y2=(-b-cmath.sqrt(d))/(2*a)
print(" The solutions are {0} and {1}".format(y1,y2))
#finding the length of python
length_of_python=(len("python"))
print("The length of characters in python is:",length_of_python)
#finding the length of dragon
length_of_dragon=(len("dragon"))
print("The length of characters in dragon is:",length_of_dragon)
#falsy comparison between the length of python and dragon
comparison=(len("python")>len("dragon"))
print("The comparison between the length of characters in python and dragon is:", comparison)
#checking the word jargon in the sentence
searching=( "jargon" in "i hope this course is not full of jargon")
print("The word jargon is found in the sentence as",searching )
#converting length of python to float and string
word="python"
word=len(word)
print("The length of the word python is:",word)
#converting to float and string
conversion_to_float=(float(word))
print("The length of the word python in float is:", conversion_to_float)
string=str(word)
print("The length of the word python in string is:", string)
#Program to identify even or odd number.
num = int(input("Enter a number: "))  
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))
# checking if thesame floor division with division
print("Checking if floor division is thesame as division:",7//3 == 2.7) 
#checking if thesame type
print(type("10")==type(10))
#checking if int('9.8') and 10 are thesame
x=int(9.8)
print((x)==10)
#Weekly earning base on number of hours
hours=input("Enter Hours:")
rate=input("Enter Rate per Hour:")
pay=float(hours)*float(rate)
print("Your weekly earning is",pay)
#calculating nunber of seconds in a years
from datetime import datetime
age = int(input('Enter the numbers of years you have lived: '))
second=age*31536000
print("Your have lived for {0} seconds".format(second))
print('1\t 1\t 1\t 1\t')
print('1\t 2\t 4\t 8\t ')
print('1\t 3\t 9\t 27\t')
print('1\t 4\t 16\t 64\t')
print('1\t 5\t 25\t 125\t')