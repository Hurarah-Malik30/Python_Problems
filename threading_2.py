#Thread Pool Executor

import concurrent.futures
import time

start = time.perf_counter()
def dosomething(second):
    print(f"Sleeping {second} sec(s)...")
    time.sleep(second)
    return f'Done Sleeping for {second}(s)...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(dosomething,1)
    # f2 = executor.submit(dosomething,1)
    # print(f1.result())
    # print(f2.result())
    secs = [5,4,3,2,1]
    # results = [executor.submit(dosomething,sec) for sec in secs]#returns a future object in the order they are completed
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    results = executor.map(dosomething,secs) #returns the result itself and in the order they were passed i.e. 5,4,3,2,1
    for result in results: #context manager automatically uses .join
        print(result)
finish= time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)") 