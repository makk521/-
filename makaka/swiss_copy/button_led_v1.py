'''
树莓派上两个button控制一个灯。点灯由单独一个线程负责.工作是处理status_que内容,当检测到按键按下时,将对应数据存入status_que.
现象:按下按键6时执行led亮灯方式1,按下按键7时执行亮灯方式2(树莓派)
'''
import RPi.GPIO as GPIO
import queue
import threading
import time
import signal

class LED:
    def __init__(self) -> None:
        self.parm_init()
        self.gpio_init()
        
        GPIO.add_event_detect(self.button_1, GPIO.RISING, callback=lambda chanel : self.update_status_que(1), bouncetime=400)
        GPIO.add_event_detect(self.button_2, GPIO.RISING, callback=lambda chanel : self.update_status_que(2), bouncetime=400)
    
    def parm_init(self):
        self.led      =   8 # 5
        self.button_1 =  6 
        self.button_2 =  7
        self.status_que = queue.Queue(10)

    def gpio_init(self):
        GPIO.setwarnings(False)	
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led, GPIO.OUT)
        GPIO.setup(self.button_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # 按键没效果改成pull_up_down=GPIO.PUD_DOWN
        GPIO.setup(self.button_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

    def _blink_1(self):
        GPIO.output(self.led,GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(self.led,GPIO.LOW)
        time.sleep(0.3)
    
    def _blink_2(self):
        GPIO.output(self.led,GPIO.HIGH)
        time.sleep(1.7)
        GPIO.output(self.led,GPIO.LOW)
        time.sleep(0.3)

    def process_que(self):
        while True:
            status = self.status_que.get()
            if status == 1:
                self._blink_1()
            elif status == 2:
                self._blink_2()
            else:
                print('Warning:illegal queue data!')

    def update_status_que(self,cmd):
        self.status_que.put(cmd)

    def my_callback(self,BUTTON):
        GPIO.output(self.led,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.led,GPIO.LOW)

# 按键检测中断，防抖时间400ms。
# GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=my_callback, bouncetime=400)

if __name__ == '__main__':
    led = LED()
    t1 = threading.Thread(target=led.process_que, args=())
    t1.start()

    signal.pause()