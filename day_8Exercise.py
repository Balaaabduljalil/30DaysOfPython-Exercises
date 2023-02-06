dog = {}
dog["Name"] = "Buddy"
dog["Colour"] = "Red"
dog["Breed"] = "Labrador Retriever"
dog["Legs"] = 4
dog["Age"] = 7
print("The added dictionaries of the dog is:", dog)
student = {'first_name':'Abduljalil' , 'last_name':'Bala' , 'gender':'male' , 'age':25 ,'is_married':'False' , 'skills':['SQL' , 'Python' , 'MongoDB' , 'Public Speaking' , 'HTML'] , 'country':'Nigeria' , 'city':'Maiduguri' , 'address':'PMB 1069 Bama street'}
print("The length of a student dictionary is:",len(student))
value_skills=student .get('skills')
print("The student value skills in the  dictionary are:",value_skills)
print("The data type for student skills in the dictionary is:",type('skills'))
student['skills'] .append('Java')
print("The new student dictionary after Java skill was added is:",student)
get_key=student .keys()
print("The student dictionary keys are:",get_key)
get_values= student .values()
print("The student dictionary values are:", get_values)
print("The changed list of tuple for student dictionary is:", student .items())
print("student dictionary item to be  deleted is:", student .popitem())
del student['country']
print("The student dictionary after country item was deleted are:",student)