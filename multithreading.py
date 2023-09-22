import time
import threading
from concurrent.futures import ThreadPoolExecutor

def func1(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)
    return sec

# Normal way to call functions which will take total time 7 seconds approx
# func1(4)
# func1(3)
# func1(2)

def main():
    time1 = time.perf_counter()

    t1 = threading.Thread(target=func1,args=[4])
    t2 = threading.Thread(target=func1,args=[3])
    t3 = threading.Thread(target=func1,args=[2])

    t1.start() # Start just start the process
    t2.start()
    t3.start()

    t1.join() 
    t2.join()
    t3.join()
    time2 = time.perf_counter()
    print(time1 - time2)

# From concurrent.futures import from ThreadPoolExecutor
def poolingTest():
    with ThreadPoolExecutor() as executor:
        f1 = executor.submit(func1,5)
        f2 = executor.submit(func1,3)
        f3 = executor.submit(func1,1)
        print(f1.result())
        print(f2.result())
        print(f3.result())

poolingTest()