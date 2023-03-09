'''
使得两个函数同时运行（异步）
'''
from threading import Thread
import time
def func1():
    while(1):
        print('1')
        time.sleep(1)   

def func2():
    while(1):
        print("2")
        time.sleep(1)

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()

# 带参数的

# from threading import Thread
# import time
# def func1(a):
#     while(1):
#         print(a)
#         time.sleep(1)   

# def func2(a):
#     while(1):
#         print(a)
#         time.sleep(1)

# if __name__ == '__main__':
#     Thread(target = func1,args=("a")).start()
#     Thread(target = func2,args=("b")).start()