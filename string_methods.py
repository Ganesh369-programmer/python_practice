str1 = "AvFdeGTVs"
str2 = "   AvFdeGTVs   "
str3 = "brnchhhhhooooooddddd !!!!!!!"
str4 = "mi_ganesh_pawar_ahe_ani_coding shikat ahe"
#upper 
print("this is a Upper character",str1.upper())

#lower
print("this is a lower character",str1.lower())

#strip :- this method removes white space before and after
print("this is a Strip charactr",str2.strip())

#rstrip
print("this is a Rstrip ",str3.rstrip("!"))

#replace
print("this is replce chararter ",str3.replace("r","e"))

#capitalization
cap1 = str4.capitalize() 
print("capitilization of line ", cap1)

#center
print(str1.center(50 , "'"))

#count
cou = str4.count("a")
print("Coounting which time the a is come ",cou)

#endswith
end = str3.endswith("!")
print(end)  #it give a true or false

#startswith
sta = str3.startswith("b")
print("Is the line is start from b or not ",sta)

#find 
print(str4.find("ahe"))   # it provide  a index of string . if he doesn't got string it returns -1

#index
print(str1.index("A"))

#title
print(str4.title()) # it convert a all strings first charater into upper case

#swapcase :- it convert upper to lower and lower to upper
print("Using a swip case ",str1.swapcase())

