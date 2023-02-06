#Level One Solution.
# 'Day 2: 30 days of python Programming'
first_name='Abduljalil'
last_name='Bala'
space=" "
full_name=last_name + space + first_name
print(full_name)
country='Nigeria'
city='Maiduguri'
age=25
year=1998
is_married=True
is_true=True
is_light_on=True
country,city,age,year = 'Nigeria','Maiduguri',25,1998
#Level Two Solution
#checking data types
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
#Length of the first name
print(len(first_name))
#comparing len of first name with last name
print(len(first_name)<=len(last_name))
#basic variable operation in python
num_one=5
num_two=4
total=num_one + num_two #addition(+)
print("The addition is: ", total)
diff=num_one-num_two
print("The difference is:", diff) #difference
product= num_one*num_two
print("The product is:", product) #product
division=num_one/num_two
print("The division is:", division) #division
remainder =num_two%num_one
print("The modular is:", remainder) #modular
exp=num_two**num_one
print("The exponential is:", exp) #exponential power 
floor_division=num_one//num_two
print("The floor_division is:", floor_division)  #floor division
#calculating the radius of the circle
from math import pi
r=30
area_of_circle=pi*r**2
print("The area of the circle with radius 30meter is:",area_of_circle)
circum_of_circle=2*pi*r
print("The circumference of the circle is:",circum_of_circle)
#Taking the radius from the user to calculate the area of the circle
radius=input("Enter the radius as:" )
new_area_of_circle=pi*r**2
print("The area of the circle from the user is:",new_area_of_circle)
