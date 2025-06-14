info = {
    'name': 'Ganesh',
    'age' : 20,
    'eligible': True
}
# list and dictionary is same beacause it uses {} bracket

print(info)

print(info.get('age'))

print(info.values())
print(info.keys())

print(info.items())


for keys , values in info.items():
    print(f"{keys} == {values}")



# dictionary method 
info.update({'age': 21})
info.update({'DOB' : '21/6/2005'})
print(info.items())


info.clear()
if(info == {}):
    print("this is empty ")
else:
    print("this is not empty ")