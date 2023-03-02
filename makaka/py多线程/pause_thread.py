'''
创建了两个进程MyThread和MyThread1，两个同时运行，且支持一个线程内暂停掉另一个线程
'''
import threading
import time

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.event = threading.Event() # 定义一个Event对象

    def run(self):
        while True:
            print('I am running')
            time.sleep(1)
            self.event.wait() # 等待标志为True或超时

class MyThread1(threading.Thread):
    def __init__(self):
        super().__init__()
        self.event = threading.Event() # 定义一个Event对象

    def run(self):
        while True:
            t.event.clear() # 清除标志，让线程暂停，即进程内控制另一进程
            print('I am running22')
            
            time.sleep(2)
            t.event.set() # 设置标志，让线程恢复
            self.event.wait() # 等待标志为True或超时

# 1进程开始运行
t = MyThread()
t.start()

t1 = MyThread1()
t1.start()

time.sleep(5)
t1.event.clear()   # 进程暂停

print('Pause thread')
time.sleep(5)

t1.event.set()     # 进程继续
print('Resume thread')