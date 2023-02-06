#Level_one
print("using for loop range(0,11)")
for i in range(0,11):
    print(i)
count=0
print("Using while loop")
while count<=10:
   
   print(count)
   count+=1
print("using for loop for range(10,-1,-1)")
for i in range(10,-1,-1):
    print(i)
k=10
print("using while loop for thesame range")
while k>=0:
    print(k)
    k-=1
print("using for loop to print #")
multiple_hash ="#"
for i in range(0,8):
    print(multiple_hash * i)
for i in range(1,9):
    for j in range(1,9):
        print("#", end=" ")
    print()
print("Performing the following operation with for loop")
for i in range(0,11):
     print(i, "x", i, "=", i*i)
print("The list of programming languages:")
for language in ["Python", "Numpy", "Pandas", "Django", "Flask"]:
     print(language)
print("The list of numbers divisiable by 2 in the range(0,101)")
for i in range(0,101):
    if i % 2==0:
        print(i)
print("The list of numbers indivisiable by 2 in the range(0,101)")
for i in range(0,101):
    if i % 2 !=0:
        print(i)

 #Level_two
sum_of_num=0
for i in range(0,101):
    sum_of_num +=i
print("The sum of range numbers is:", sum_of_num)
#sum of even and odd numbers in the range
sum_even=0
sum_odd=0
for i in range(0,101):
    if i % 2==0:
        sum_even +=i
    else:
        sum_odd +=i
print("The sum of an even numbers is:",sum_even)
print("The sum of an odd number is:",sum_odd)
#Level_three
print("list of countries that end with Land are:")
countries=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia','Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South','Kuwait','Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
countries_list = countries
for country in countries_list:
    if "land" in country:
        print(country)

print("The reverse added list of fruits are:")
list_of_fruit=["Banana", "Orange", "Mango", "Lemon"]
reverse = []
for i in range(3,-1,-1):
    reverse.append(list_of_fruit[i])
    print(reverse)