# cancatenation of Thirty Days of Python 
first_word="Thirty"
second_word="Days"
third_word="of"
fouth_word="Python"
space=" "
full_sentence=first_word + space + second_word + space + third_word + space + fouth_word
print("The cancatenated string is:",full_sentence)
#cancatenation of coding for all. 
coding="Coding"
word_off= "for"
all= "all"
full_statement= coding + space + word_off + space + all
print("The cancatenated string is:",full_statement)
company ="Coding for all"
print(company)
print("The length of the word company is:",len(company))
print("The upper case of the string is:", company .upper())
print("The lower case of the string is:", company .lower())
print("The capitalize form of the string is:",company .capitalize())
print("The title form of the string is:",company .title())
print("The swapcase of the string is:", company .swapcase())
print("The slicing of the string is:",company[0:6])
sub_string="Coding"
print("The index is:",company .index(sub_string))
new_string="Coding for Everyone"
print(new_string .replace("Everyone" , "All"))
print(company .split())
company_two="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon,"
print(company_two .split(' , '))
print("The first character in the index string is:",company[0])
print("The last character in the index string is:",company[-1])
print("The character at index 10 in the string is:",company[10])
print("The index of  'C' in coding for all is:", company .index("C"))
print("The index of 'F' in coding for all is:", company .index("f"))
new_string="You cannot end a sentence with because because because is a conjunction"
print("The index for first occurrence of a word because is:", new_string .find("because"))
print("The last index of the word because occurrance is:", new_string .rindex("because"))
print("The slicing of the word are:", new_string[31:54])
print("Does this sentence of new_string start with word coding:",new_string .startswith("coding"))
print("Does this sentence of new_string end with word coding:", new_string .endswith("coding"))
string_one="   Coding For All   "
print("That remove the leading and trailing whitespace as:",string_one.strip())
challange="thirty_days_python"
print("Is the only string that resulted to true identifier:",challange .isidentifier())
python_libraries=['Django', 'Flask', 'Bottle','Pyramid','Falcon']
print("The joined sliced are:",  ' # ' .join(python_libraries))
print("Name\t Age\t Country\t City")
print("Asbeneh\t 250\t Finland\t Helsinki")
a="radius"
b="area"
s=22
t=7
w=2
v=10
print("{}={}".format(a,v,a=v))
radius = 10
pi = (3.14)
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.0f} meters square'.format(radius, area) 
print(formated_string)
#string formatting method
x=8
y=6
print("This are the formated string operation")
print("{}+{}={}".format(x,y,x+y))
print("{}-{}={}".format(x,y,x-y))
print("{}*{}={}".format(x,y,x*y))
print("{}/{}={:2f}".format(x,y,x/y))
print("{}%{}={}".format(x,y,x%y))
print("{}//{}={}".format(x,y,x//y))
print("{}**{}={}".format(x,y,x**y))