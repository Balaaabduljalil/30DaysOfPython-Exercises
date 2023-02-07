#Level_one
#quation_1
def sum_of_two_numbers(a,b):
    return a+b
#quation_2
def area_of_circle(r):
    return 3.14*r*r
 #quation_4   
def celsius_to_fehre(celsius):
    return (celsius*9/5)+32
#quation_5    
def season_of_months(month):
    if month in ["september","october","november"]:
        print("Autumn")
        
  
    if month in ["december","january","february"]:
        print("winter")
   
    if month in ["march","april","may"]:
        print("spring")
    else:
        print("summer")
 #quation_6
def slope (x1,x2,y1,y2):
    m=(y2-y1)/(x2-x1)
    return m
 #quation_7 
def quadratic_equation(a,b,c,d):
    d=b*b-4*a*c
    x1=(-b+d)/(2*a)
    x2=(-b-d)/(2*a)
    print(x1,x2)
 #quation_8
def new_list(list):
     for i in list:
         print(i)
 #quation_9
def list_reverse(a):
     return a[::-1]
#quation_10
def list_of_capital_terms(a):
    for i in a:
        a[a.index(i)]=i.capitalize()
        return a
#quation_11
def add_item(price, tba):
    price.append(tba)
    return price
#quation_12
def remove_item(price, tba):
    price.remove(tba)
    return price
 #quation_13
def sum_of_numbers(high):
     sum_of_nunbers=0
     for i in range(high + 1):
         sum_of_numbers +=i
         return sum_of_nunbers
 #quation_14
def sum_of_odds(high):
    sum_of_odd_nunbers=0
    for i in range(high + 1):
        if i % 2==1:
            sum_of_odd_nunbers +=i
            return sum_of_odd_numbers
  #quation_15
def sum_of_even(high):
     sum_of_even_numbers=0
     for i in range(high + 1):
         if i % 2==0:
             sum_of_even_nunbers +=1
             return sum_of_even_numbers
 #level_two
def evens_no_and_odds_no(high):
     odds=0
     evens=0
     for i in range(high + 1):
         if i % 2==0:
             even+=i
         else:
             odd+=i
             print(odds,evens)
def factorial(x):
         fact=1
         for i in range(x+1):
             fact*=i
             return fact
def is_empty(c):
 if check:
     return True 
 else:
     return False
def mean(dataset):
 return sum(dataset)/len(dataset)
def median(dataset):
 data=sorted(dataset)
 index=len(dataset)//2
 if len(dataset)%2!=0:
     return data[index]
     return (data[index-1] + data[index])/2
def mode(dataset):
 frequency={}
 for value in dataset:
     frequency[value]=frequency .get(value,0)
     most_frequency=max(frequency .value())
     modes=[key for key, value in frequency .items() if value == most_frequent]
     return modes
def variance(dataset):
 n=len(dataset)
 mean=sum(dataset)/n
 for x in dataset:
     deviations=(x-mean)**2
  
 variance = sum(deviation)/n
 return variance
def standard_deviation(dataset):
 var=variance(dataset)
 standard_deviation=var**0.5
 return standard_deviation
 #Level_three
def is_prime(n):
 if n<=1:
     return False
     max_div =math.floor(math.sqrt(n))
 if i in range(2,1+max_div):
     if n%i==0:
         return False
         return True
def check_list(list):
    return len(set(set_list))==len(list)
def checkList(lst):
 

    ele = lst[0]

    chk = True
 

    # Comparing each element with first item

    for item in lst:

        if ele != item:

            chk = False

            break
 

    if (chk == True):

        print("Equal")

    else:

        print("Not equal")
list_data = countries_data.data
total_language_initial=[]
for i in list_data:
    total_language_initial.extend(i["language"])
    print("language=", len(set(total_language_initial)))
    counts={}
    for i in total_language_initial:
        counts[i]=counts.get(i,0)+1
        
def sort_dict_by value(d, reverse=False):
    return dict(sorted(d.items())), key=lamda x:x[i], reverse=reverse))
    counts=sort_dict_by_value(counts, True)
    for i in list (counts, items())[:20]:
        print(i)
        population {}
        for i in list_data:
            populations[i["name"]]=i["population"]
            populations=sort_dict_by_value(populatiobs,True)
            for i in list(populations:items())[:20]:
                print(i)

