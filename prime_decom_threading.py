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
        total_work(self.name, self.begin, self.end)
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

if __name__ == '__main__':
    threads = []
    start = time.time()
    for i in range(1,6):
        thread = worker("thread"+str(i), 1+((i-1)*10000), 1+i*10000)
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
    totalTime = time.time() - start
    print("Total time taken for this task is %s seconds" % (totalTime))
