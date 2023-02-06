#Level_one 
empty_tuble=()
name_sisters=("Maryam","Sumaiya","Shamsiya","Fatima","Farida")
name_brothers=("Affan", "Shittu", "Aliyu","Nasiru")
siblings= name_sisters + name_brothers
print("My family siblings are:",siblings)
print("My family have numbers of siblings:",len(siblings))
parent_names=("Bala","Hauwa")
family_members =siblings + parent_names
print("The entire family members are:",family_members)
#Level_two
print("My parents names are:",parent_names)
print("My siblings names are:",siblings) 
fruits=("Orange", "Mango", "Cashew","Pawpaw")
vegetables=("Tomoto","Green Beans","Garlic",)
animal_products=("Meat","Egg","Poultry","Milk")
food_stuff_tp=fruits + vegetables + animal_products
print("The joined food stuff are:",food_stuff_tp)
food_stuff_lt=food_stuff_tp
print("The assigned change about is:",food_stuff_lt)
length=(len(food_stuff_tp))
length_round=int((length)/2)
print("The middle item in the food stuff list is:",food_stuff_tp[length_round])
print("The first three items on the list are:",food_stuff_tp[:3])
print("The last three items on the list are:",food_stuff_tp[-3:])
del food_stuff_tp
print("No items in the tuple after deleted.")
nordic_countries=('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Checked if Estonia is in tuple of nordic countries:", 'Estonia' in nordic_countries)
print("Checked if Iceland is in the tuple of nordic countries:", 'Iceland' in nordic_countries)
