import multiprocessing

# def my_fucn():
#     print("Hrllo from proccess ", multiprocessing.current_process().name)
#     process = multiprocessing.Process(target= my_fucn)
#     process.start()
#     process.join()

from multiprocessing import pool 
def process_task(task):
    print(f"Task Processed {task}")

if __name__ == '__main__':
    j = []
    for i in range(11):
        j.append(i)

    
    with pool(processes = 4 ) as pool:
        results = pool.map(process_task , j)