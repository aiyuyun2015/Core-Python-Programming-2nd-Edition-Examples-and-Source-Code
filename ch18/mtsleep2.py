#!/usr/bin/env python

import thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()  ###-> indicate the main function this thread is completed.

def main():
    print 'starting threads...'
    locks = []
    nloops = range(len(loops))

    print("nloops:{}".format(nloops))

    #init two locks and append them to a list called locks
    for i in nloops:
        lock = thread.allocate_lock()   ##init lock object.
        ##in fact, acquire the lock
        lock.acquire() 
        locks.append(lock)

    #spawn thread with arguments, kwargs, the arguments is tuple, which set the parameters in the loop function
    for i in nloops:
        thread.start_new_thread(loop, 
            (i, loops[i], locks[i]))

    #check the lock status sequencially
    
    for i in nloops:
        while locks[i].locked(): pass

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
