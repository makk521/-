'''
线程一将20个数据填入大小为10的队列中,超出后数据等待
线程二将队列数据每隔一秒弹出一个,直到全部删除
'''
import queue
from threading import Thread
import time
q = queue.Queue(maxsize=10)
def add_ele():
    for i in range(20):
        q.put(i,block=True)
        print(q.queue)

def del_ele():
    time.sleep(1)
    while not q.empty():
        time.sleep(1)
        q.get()
    
if __name__ == '__main__':
    Thread(target = del_ele).start()
    Thread(target = add_ele).start()