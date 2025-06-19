#For I/O bound Tasks

import time
import threading
start = time.perf_counter()
# print(start)
def dosomething(second):
    print(f"Sleeping {second} sec(s)...")
    time.sleep(second)
    print('Done Sleeping')

# dosomething()
# dosomething()

#create thread for each function call
# t1 = threading.Thread(target=dosomething)
# t2 = threading.Thread(target=dosomething)

# calling the thread
# t1.start()
# t2.start()

#finish the threads before moving on
# t1.join()
# t2.join()


#making threads to run function 10 times
threads = []
for _ in range(10):
    t = threading.Thread(target=dosomething,args=[1.5])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join() #we created a list that holds our threads and now we a re loopin over our threads to join them i.e. wait for them to finish

finish= time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")