#Level_one
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print("The length of the IT companies is:",len(it_companies))
new_it = it_companies .add('Twitter')
print("The IT companies after Twitter was added are:",it_companies)
it_multiple={'Cisco','Dell', 'Cognizant', 'Alphabet','Netflix'}
it_companies .update(it_multiple)
print("The list of IT companies after multiples were added are:",it_companies)
it_companies .remove("Dell")
print("The list after Dell company was remove are:", it_companies)
print("In remove method, if the item to be remove is not in the list it will raise an error but discard do not raise any error")
#Level_two
x= A .union(B)
print("The union of A and B are:",x)
print("The intersection of A and B is:", A. intersection(B))
print("Is A aubset of B:", A. issubset(B))
print("Are A and B disjoint:", A .isdisjoint(B))
y= B .union(A)
print("The union of B with A is:", y)
print("The symmetric difference between A and B is:", A .symmetric_difference(B))
#deleting the sets
del x
del y
#Level_three
new_set = set(ages)
print("The converted list to set are:",new_set)
print("The length of the ages list is:", len(ages))
print("The length of the converted ages list to set is:", len(new_set))
ages_comparison=(len(ages)==len(new_set))
print("The length comparison for the ages list and set is:", ages_comparison)
print("A String is a collection of alphabets, words or other character while both list and tuple are just collection of ordered data and then set is a collection of unordered data")
def printWords(l):


    for i in l:

        print(i)

str = "I am a teacher and I love to inspired and teach poeple"

s = set(str.split(" "))
print("The numbers of unique words in the sentence is:",len(s))