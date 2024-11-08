my_dict={'Andrey': 3091986, 'Vasya': 4051986, 'Petya': 1081986}
print(my_dict)
print(my_dict['Andrey'])
print(my_dict.get('Kamila'))
my_dict['Anton']=2021986
my_dict['Sasha']=1091986
print(my_dict)
del my_dict['Andrey']
print(my_dict)
my_dict['Andrey']=3091986
print(my_dict['Andrey'])

my_set={1,2,3,4,5,1,2,3,4}
print(my_set)
list_=(6,6,7,7,7)
list_=set(list_)
print(list_)
print(list_.discard(1))
print(list_)
print(my_set)