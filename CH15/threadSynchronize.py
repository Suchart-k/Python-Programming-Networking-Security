from threading import Thread
import threading
import time

class myThread (Thread):
    def __init__(self, threadID, name, counter):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def printTime(self, threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print ("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
        
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        self.printTime(self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
    
print ("Exiting Main Thread")
