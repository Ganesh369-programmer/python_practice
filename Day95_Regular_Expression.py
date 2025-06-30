import re
pattern = r"world"
text = "Hello world "

match = re.search(pattern , text )
print(match)
if match:
    print("Match found ")

else:
    print("Match not Found !")


############################################################
pattern1 = r"cat , hat"
text1 = "The cat is in the hat"

matches = re.findall(pattern1 , text1 )

print(matches)

############################################################
pattern = r"[a-z]+at"
text = "The cat is in the hat "
matches = re.findall(pattern , text)
print(matches)

new_text = re.sub(pattern , "dog" , text)
print(new_text)

############################################################
text3 = "The email address is ganesh3692005@gmail.com"
pattern3 = r"\w+@\w+\.\w+"

matches3 = re.search(pattern3 , text3)

if matches3:
    email = matches3.group()
    print(email)