import time
print(time.time())

t = time.localtime()
formatted_time = time.strftime("%d - %m - %Y , %H : %M : %S" , t)
print(formatted_time)