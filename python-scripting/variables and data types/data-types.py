x=5
print(id(x)) # Print memory location of variables
y=x
print(id(y))
z=7
print(id(z))
x=3
y=5.6
z=3+4j
#x=3;y=5.6;z=3+4j
print(x)
print(y)
print(z)
#print(x,y,z)
print(x,type(x))
print(y,type(y))
print(z,type(z))

lang_name='python scripting'
print(lang_name,type(lang_name))

my_name="sunil"
print(my_name,type(my_name))

my_value=True  # True, False are boolean , true and false are strings. "True" and "False" is string not boolean
print(my_value,type(my_value))

x=56
print(x,type(x))
y=str(x)
print(y,type(z))
z=bool(x)
print(z,type(z))
p=0
print(p,type(p))
q=bool(p)
print(q,type(q))

x=5.6
print(int(x))
my_name="sunil"
print(my_name,type(my_name))
#print(int(my_name))
bool(None)

'''
Any data type can be converted to boolean
bool(any_data_type)=True or False

bool(empty)=False ==> bool(0),bool(None),bool([]),bool(()),bool({})
bool(non-empty)=True

Any Data type can be converted to string but reverse is not always can be done
Numbers. Integers can be converted to strings but version e.g. 1.2.3.4 can't be converted to numbers, but need to represent as strings

'''
