import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = time.strftime('%H')
print(timestamp)

timestamp = time.strftime('%M')
print(timestamp)

#hour = int(time.strftime('%H'))
hour = int(input("Enter the number :"))
print(hour)
if (hour >=0 and hour < 12):
    print("Good Morning sir!")
elif (hour >= 12 and hour < 17):
    print("Good Evening sir ")
elif (hour >= 17 and hour < 24):
    print("Good Night sir")
else:
    print("Kuchh to gadbad hai ddaya")