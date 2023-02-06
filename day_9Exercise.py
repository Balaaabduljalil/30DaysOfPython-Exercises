#Level_one
age=int(input("Enter your age:"))
if age>=18:
    print("You are old enough to drive.")
else:
    print("You need to wait", 18-age, "years to drive.")
    
your_age=int(input("Enter your age:"))
my_age=18
if your_age==my_age:
   print("We are of thesame age.")
elif your_age>my_age:
   print("You are", your_age-my_age, "years older than me.")
else:
   print("I am", my_age-your_age, "years older than you.")
   
a=int(input("Enter your first number:"))
b=int(input("Enter your second number: "))
if(a<b):
    print("{0} is smallest than {1}".format(a,b))
elif(b<a):
    print("{1} is larger than {0}".format(b,a))
else:
    print("{0} and {1} are equal".format(a,b))
    
#Level_two
marks = float(input("Enter Student score: "))
#checking grade from the score 
if marks > 80:
    print("Grade: A")
elif marks >= 80 and marks < 89:
    print("Grade: A")
elif marks >= 70 and marks < 80:
    print("Grade: B")
elif marks >= 60 and marks < 70:
    print("Grade: C")
elif marks >= 50 and marks < 60:
    print("Grade: D")
elif marks >= 40 and marks < 50:
    print("Grade: E")
else:
    print("Grade: F")
 #checking the sesson of a months
month = input("Enter the month of the year  (e.g. January, February etc.): ")

if month in ('January', 'February', 'December'):
	season = 'winter'
elif month in ('April', 'March', 'May'):
	season = 'spring'
elif month in ('July', 'August', 'June'):
	season = 'summer'
else:
	season = 'autumn'
print("The Season is:",season)
#checking if the fruit exist in the list.
fruits = ['Banana' , 'Orange' ,'Mango' ,'Lemon']

user_input = 0

try:
    user_input = (input('Enter your favorite fruit: '))
except ValueError:
    print('The provided input is not a valid fruit')

if user_input in fruits:
    print('The fruit alrewdy exist in the list')
else:
    fruits.append(user_input)

print(f'Updated Fruits List {fruits}')
#Level_three
person = { "first_name":"Abduljalil" ,"last_name":"Bala" , "age":25 , "country":"Nigeria" , "is_married":False , "skills":["Javascript", "React", "Node", "MongoDB", "Python"], "address":{ "street":"Bama Street", "Postcode":"PMB 1069"}}
if person["skills"]:
    print("The middle skills in the list of this person skills is : " , person["skills"][len(person['skills'])//2])
    print("Is python in this person list of skills:","Python" in person["skills"])
if ["Javascript","React"]==person["skills"]:
     print("He is front end developer.")
elif["Node", "Python", "MongoDB"]==person["skills"]:
    print("He is a backend developer")
elif["React","Node","MongoDB"]==person["skills"]:
    print("He is a fullstack developer")
else:
    print("unknown Tittle")
if person["is_married"]:
    print(person["first_name"], person["last_name"], "lives in", person["country"], "he is married.")
else:
    print(person["first_name"], person["last_name"], "lives in", person["country"], "he is not married.")