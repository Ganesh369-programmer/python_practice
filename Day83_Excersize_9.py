import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# while 1 :
#     print("Enter the Text ")
#     s = input()
#     speaker.Speak(s)


user = ["Ganesh" , "Suresh " , "Ramesh " , "Raju" , " Harry Bhai " , "Elvish Bhai " ]

for i in range(len(user)):
    speaker.Speak(f"Shoutout to {user[i]}")