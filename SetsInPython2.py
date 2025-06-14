city1 = {"tokoyo", "madrid" , "berlin" , "delhi"}
city2 = {"tokoyo", "seoul" , "kabul", "madrid" }

# print("isdisjoint") #it checks the item in set1 is present in set2 or not . if item is available then it returns "False" and if item is not availble then it return "True"
# city3 = city1.isdisjoint(city2)
# print(city3)


print("issuperset")
print(city1.issuperset(city2))

city3 = {"berlin" , "delhi" }
print(city1.issuperset(city3))

if(city1.issuperset(city3) == True):
    print("yes . the item of city 3 is available in city1")
else:
    print("city3 chya value city1 madhye available nahi ahe.")


city4 = {"tokoyo", "madrid" , "berlin" , "delhi"}
print(city1.issubset(city4))

city1.add("Up")
print(city1)
if "Up" in city1:
    print("available")
else:
    print("Not availble ")


city5 = {"mp","Bihar" , "rajasthan" , "haryana"}
city2.update(city5)
print(city2)

city2.remove("mp")
print(city2)

item = city2.pop()
item = city2.pop()
print(city2)







