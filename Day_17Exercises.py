#Program to unpack the first five countries and store then in as variable nordic_countries while the rest to be store as es and ru respectively. 
names=['Finland','Sweden','Norway','Denmark','Iceland','Estonia','Russian']
try:
    *nordic_countries,es,ru=names
    print(nordic_countries,es,ru)
except Exception as output:
     print(output)