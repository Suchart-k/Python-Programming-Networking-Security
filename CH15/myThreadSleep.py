from threading import Thread
import time

class myThread (Thread): #Extending Thread class
    def __init__(self, threadID, name, counter):
        Thread.__init__(self) #Overriding __init__ method
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def printTime(self, threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print ("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

    def run(self): #Overriding run method
        print ("Starting " + self.name)
        self.printTime(self.name, self.counter, 5)
        print ("Exiting " + self.name)
        
# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print ("Exiting Main Thread")


