info = {"Ganesh", 1 , 2 , False , 9.8}


# for item in info:
#     print(item)

cities = {"Tokoyo" , "madrid" , "berlin" , "delhi"}
cities2 = {"Tokoyo" , "seoul" , "kabul" , "madrid"}

print(cities)
print(cities2)
print("\n press 1 :- Union code ")
print("\n press 2 :- Intersection method ")
print("\n press 3 :- Summetric_difference method ")
print("\n press 4 :- Difference method ")
x = int(input("Enter the Number "))

match x :
    case 1:
        print("\n Union code ")
        city = cities.union(cities2)
        print(city)

        cities.update(cities2)
        print(cities)

    case 2:
        print("\n Intersection method ")
        city = cities.intersection(cities2)
        print(city)

        cities.intersection_update(cities2)
        print(cities)

    case 3:
        print("\n Summetric_difference method ")
        city = cities.symmetric_difference(cities2)
        print(city)

        cities.symmetric_difference_update(cities2)
        print(cities)

    case 4:
        print("Difference method ") #this is elimant the element which is present in the second set 
        city = cities.difference(cities2)
        print(city)

        cities.difference_update(cities2)
        print(cities)




