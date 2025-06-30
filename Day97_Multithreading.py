import threading
# import time 
# def main():
#     time.sleep(2)
#     print("Hello world ")

# def main1():
#     time.sleep(2)
#     print("Hello world 2")

# def main2():
#     time.sleep(2)
#     print("Heloo World 3")

# # main()
# # main1()
# # main2()

# t1 = threading.Thread(target=main)
# t2 = threading.Thread(target=main1)
# t3 = threading.Thread(target=main2)
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()

def increment(counter , lock):
    for i in range(10000):
        lock.acquire()
        counter += 1
        lock.release()



def thread_task(task):
    print(f"task processed :{task}")

if __name__ == '__main__':
    
    tasks = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
    th = []
    for t in tasks:
        t1 = threading.Thread(target= thread_task , args= (t , ))
        th.append(t1)
        t1.start()

    for thread in th:
        thread.join()
        

    counter = 0
    lock = threading.Lock()

    threads = []
    for i in range(2):
        thread= threading.Thread(target=increment , args=(counter , lock ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Counter value",counter)

    

