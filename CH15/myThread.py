from threading import Thread

class myThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print("Hello, my name is %s\n" %self.getName())

thread1 = myThread("Thread 1")
thread2 = myThread("Thread 2")
thread3 = myThread("Thread 3")
thread1.start()
thread2.start()
thread3.start()


