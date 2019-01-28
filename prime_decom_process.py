#!/usr/bin/python

import sys
import multiprocessing
import time
from math import floor, sqrt

sys.stdout = open('processing_log.txt', 'wt')

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

def total_work(processNum, begin, end):
    for x in range(begin, end):
        print("%s = %s, done by Process %s" % (x, fac(x), processNum))
        
if __name__ == '__main__':
    jobs = []
    start = time.time()
    for i in range(1,6):
        process = multiprocessing.Process(target=total_work, args=(i, 1+((i-1)*10000), 1+i*10000))
        jobs.append(process)
        process.start()

    totalTime = time.time() - start
    print("Total time taken for this task is %s seconds" % (totalTime))
