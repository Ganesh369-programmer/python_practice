
import this
txt = "for only {price:4f} dollors "
print(txt.format(price = 29))


price = 49.099990
txt = f"for only {price:2f} dollar!"
print(txt)

name = "Ganesh pawar "
age = "19"
learn = "Python "
study = "Computer engineering "

print(f"Hello ! I am {name} , my age is {age} , I am trying to learn the {learn}. and Education in {study} ")

def sqare(n):
    ''' Takes the square output every wherer, anytime , anything and everbody ,I am Ready '''
    print(n**2)

sqare(5)

print(sqare.__doc__)

print(dir(this))
