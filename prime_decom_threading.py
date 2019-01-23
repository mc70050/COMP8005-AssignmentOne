#!/usr/bin/python

# This is Assignment 1 for COMP 8005
# The objective of this assignment is to compare the process speed
# of using multi-threading techniques and multi-processing techniques
# to do a certain time-consuming task.
#
# In this particular python executable, multi-threading is used to do prime
# number decomposition. Time consumed will be calculated and printed out to the
# user at the end.

import sys
import time
import threading
from math import floor, sqrt

sys.stdout = open('threading_log.txt', 'wt')

class worker(threading.Thread):
    def __init__(self, name, begin, end):
        threading.Thread.__init__(self)
        self.name = name
        self.begin = begin
        self.end = end
    def run(self):
        print >> sys.stdout, "Starting: %s" % (self.name)
        threadLock.acquire()
        total_work(self.name, self.begin, self.end)
        threadLock.release()
# This function returns the prime number decomposition of the argument 'n'
# This segment of code was copied from https://rosettacode.org/wiki/Prime_decomposition#Python
def fac(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n//q) or [n]

def total_work(threadName, begin, end):
    for x in range(begin, end):
        print("%s = %s, done by %s" % (x, fac(x), threadName))

###############################

threadLock = threading.Lock()
threads = []

thread1 = worker("thread1", 1, 10000)
thread2 = worker("thread2", 10001, 20000)
thread3 = worker("thread3", 20001, 30000)
thread4 = worker("thread4", 30001, 40000)
thread5 = worker("thread5", 40001, 50000)


start = time.time()

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
threads.append(thread5)

for t in threads:
    t.join()

totalTime = time.time() - start
print("Total time taken for this task is %s seconds" % (totalTime))
