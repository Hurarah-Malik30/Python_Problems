#For CPU bound tasks:all tasks start at the same time

import multiprocessing 
import concurrent.futures
import time
import threading
start = time.perf_counter()

def dosomething(seconds):
    print(f"Sleeping {seconds} sec(s)...")
    time.sleep(seconds)
    return f'Done Sleeping for {seconds} secs'

# p1 = multiprocessing.Process(target=dosomething)
# p2 = multiprocessing.Process(target=dosomething)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# processed = []
# for _ in range(10):
#     p = multiprocessing.Process(target=dosomething,args=[1.5])
#     p.start()
#     processed.append(p)

# for process in  processed:
#     process.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
    # f1 = executor.submit(dosomething,1)
    # print(f1.result())

    # results = [executor.submit(dosomething,1) for _ in range(10)]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    secs = [5,4,3,2,1]


    results = [executor.submit(dosomething,sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())



    # results = executor.map(dosomething,secs)
    # for result in results:
    #     print(result)

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} sec..')
