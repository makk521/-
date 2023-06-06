"""
红绿灯模拟
"""
import time
import random
import threading
from threading import Thread,Event

class Car_Thread():
    def __init__(self,Thread_name,event) -> None:
        self.name = Thread_name
        self.event = event
    
    def _run(self):
        time.sleep(random.uniform(1, 10))
        print(f'{self.name}已到达')
        self.event.wait()
        print(f'{self.name}已通过')
    
if __name__ == '__main__':
    light_event = Event()
    Thread_list = []

    for i in range(11):
        Thread_list.append(Car_Thread('Car' + str(i),light_event))
    for thread in Thread_list:
        Thread(target=thread._run, args=()).start()

    while threading.activeCount() > 1:
        light_event.clear() 
        print('红灯亮起') 
        time.sleep(3)
        light_event.set()
        print('绿灯亮起')
        time.sleep(1)

