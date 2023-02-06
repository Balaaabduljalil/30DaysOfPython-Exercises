#python version 3.9.7
#question_2
print (3+4) # addition(+)
print (3-4) #subtraction (-)
print(3*4) #multiplication(*)
print (3%4) #modulus (%)
print (3/4) #division (/)
print (3**4) #exponemtial
print(3//4) # float division
#question_3
print ("Abduljalil") #My_name
print("Bala") # family_name
print ("Nigeria") #Country
print ("I am enjoying 30 days of python") #Sentence
#question_4
print (type(10)) #int
print(type(9.8)) #float
print (type(3.14)) #float
print(type(4-4j)) #complex
print (type(['Asabeneh','python','finland'])) #list
print(type("Abduljalil")) #string
print (type("Bala")) #string
print (type("Nigeria")) #string
#Example of different data types.
print(type(-3)) #interger 
print(type(1.56)) #float
print(type(3+6j)) #complex
print(type("ADSA")) #string
print(type(False)) #Boolean
print(type([1,2,3])) #list
a =(1,2,4)
print(type(a)) #tuple
print(type({3,2,7,6})) #set
print(type({"Place": "London"})) #dictionaries
#calculating Euclidian distance of two given points. 
import math
point_one = [2, 3]
point_two= [10, 8]
distance = math.sqrt( ((point_one[0]-point_two[0])**2)+((point_one[1]-point_two[1])**2) )

print("The Euclidian distance is:",distance)
