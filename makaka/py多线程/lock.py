'''
运行100个进程操作同一个值，需要进程锁锁住值以使同一时间只有一个进程操作该值，避免了数据不同步。
其原理可以通过执行锁前加一个print(1)看出，所有进程都已执行这一步，但当前counter_lock.acquire()
不成立（上一个进程还没release），所以都等着。
'''
import  threading   
import  time   

counter = 0 
counter_lock = threading.Lock() #只是定义一个锁,并不是给资源加锁,你可以定义多个锁,像下两行代码,当你需要占用这个资源时，任何一个锁都可以锁这个资源 
counter_lock2 = threading.Lock()  
counter_lock3 = threading.Lock() 

#可以使用上边三个锁的任何一个来锁定资源 

class  MyThread(threading.Thread):#使用类定义thread，继承threading.Thread 
     def  __init__(self,name):   
        threading.Thread.__init__(self)   
        self.name = "Thread-" + str(name) 
     def run(self):   #run函数必须实现 
        global counter,counter_lock #多线程是共享资源的，使用全局变量 
        time.sleep(1); 
        # 测试
        print(1)  
        if counter_lock.acquire(): #当需要独占counter资源时，必须先锁定，这个锁可以是任意的一个锁，可以使用上边定义的3个锁中的任意一个 
            counter += 1    
            print("I am %s, set counter:%s"  % (self.name,counter)   )
            # 测试
            # time.sleep(1)
            counter_lock.release() #使用完counter资源必须要将这个锁打开，让其他线程使用 

if  __name__ ==  "__main__":   
    for i in range(1,101):   
        my_thread = MyThread(i) 
        my_thread.start()