import RPi.GPIO as GPIO
import time

LED     =   8
BUTTON  =   7

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # 按键没效果改成pull_up_down=GPIO.PUD_DOWN

def my_callback(BUTTON):
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED,GPIO.LOW)

# 按键检测中断，防抖时间400ms。
GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=my_callback, bouncetime=400)

if __name__ == '__main__':
    while(True):
        if (1==2):
            print(1)