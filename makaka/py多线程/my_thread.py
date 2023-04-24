'''
使得两个函数同时运行（异步）
'''
# from threading import Thread
# import time
# def func1():
#     while(1):
#         print('1')
#         time.sleep(1)   

# def func2():
#     while(1):
#         print("2")
#         time.sleep(1)

# if __name__ == '__main__':
#     Thread(target = func1).start()
#     Thread(target = func2).start()

# 带参数的

from threading import Thread
import time
def func(msg):
    while(1):
        print(msg)
        time.sleep(1)   

<<<<<<< HEAD
if __name__ == '__main__':
    Thread(target = func,args=("a")).start()
    # Thread(target = func,args=("b")).start()

    while(1):
        print(1)
        time.sleep(1)
=======
# if __name__ == '__main__':
#     Thread(target = func,args=("a",)).start()
#     Thread(target = func,args=("b",)).start()
>>>>>>> 38347124710651162689bcea762a2157db701119
