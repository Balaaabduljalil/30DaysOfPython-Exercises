#Level_one challanges
empty_list=()
students_name=["Ibrahim", "Adamu","Isah","Aisha","Maryam", "Yahaya", "Jamilu"]
print("The length of the  variable list is:",len(students_name))
print("The first item in the variable list is:",students_name[0])
print("The middle item in the variable list is:",students_name[3])
print("The last item in the variable list is:",students_name[-1])
mixed_data_types=("Abduljalil",25,1.5,"Single", "Maiduguri,Borno state")
it_companies=["Facebook", "Google","Microsoft", "Apple", "IBM","Oracle","Amazon"]
print("The list of the IT companies are:", it_companies)
print("The length of the IT companies are:",len(it_companies))
print("The first IT company in the list is:",it_companies[0])
print("The middle company in the list is:",it_companies[3:5])
print("The last IT company in the list is:",it_companies[-1]) 
print("The join list of the companies are:", '# ' .join(it_companies))
print("Does Google company exist in the list of IT companies:", 'Google' in it_companies)
print("The sort form of the IT companies are:",sorted(it_companies))
it_companies .reverse()
print("The reverse of the IT companies in descending order are:",it_companies)
print("The slice of the first three reverse IT companies are:",it_companies[-3:])
print("The slice of the last three IT companies are:", it_companies[:3])
del it_companies[0]
print("The list after removing the first company is:",it_companies)
del it_companies[4]
print("The companies list after removing the middle company are:",it_companies)
del it_companies[-1]
print("The companies list after removing the last company are:",it_companies)
del it_companies[:6]
print("The list after removing all companies in the list is:",it_companies)
it_companies .clear()
print("The companies list after destroy is:",it_companies)
front_end=["HTML", "CSS","JS","React","Redux"]
back_end=["Node", "Express", "MongDB"]
full_stack = front_end + back_end
print("The joined full stack program are:",full_stack)
full_stack .insert(5, "Python")
full_stack .insert(6, "SQL")
print("The update full stack list after python are SQL was added are:",full_stack)
#Level_two challanges
ages=[19,22,19,24,20,25,26,24,25,24]
ages. sort()
print("The sorted ages in the list are:",ages)
my_minimum=min(ages)
print("The minimum age in the list of ages is:",my_minimum)
my_maximum=max(ages)
print("The maximum age in the list of ages is:",my_maximum)
ages .append(my_minimum)
ages .append(my_maximum)
print("The ages list after minimum and maximum ages were added is:",ages)
import statistics

student_ages = ages
median_age = statistics.median(student_ages)
print("The median of the ages list is:",median_age)
from statistics import mean 

std_mean = ages

std_sum = sum(std_mean)

ages_mean = std_sum/len(std_mean)
print("Average age of the list:",ages_mean) 
min_average=my_minimum -ages_mean
print("The absolute difference between minimum age with the average is:",abs(min_average))
max_average=my_maximum-ages_mean
print("The absolute difference between the maximum age and the average is:",abs(max_average))
print("Is the absolute value of min_average thesame as max_average:",abs(min_average)==abs(max_average))
range=my_maximum-my_minimum
print("The range of the ages list is:",range)
countries=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia','Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South','Kuwait','Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
print("The length of the selected countries from the countries list is:",len(countries))
middle=int(len(countries)/2) 
print("The middle country in the countries list is:",countries[middle]) #middle country
first_half=int(len(countries)/2)-1
print("The first list half of countries list are:",countries[:first_half]) #first half 
print("The second half of the countries list are:",countries[middle:]) #second half