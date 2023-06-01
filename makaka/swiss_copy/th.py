import threading
import time
class MyThread(threading.Thread):
    def __init__(self, name, n):
        #super(MyThread, self).__init__()
        self.name = name
        self.n = n
    def run(self):
        while True:
            print("Thread ", self.name, "is running")
            time.sleep(self.n)
def main():
    t1 = MyThread("t1", 3)
    t2 = MyThread("t2", 2)
    t1.start()
    t2.start()
if __name__ == "__main__":
    print("嗨客网(www.haicoder.net)")
    main()