import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # 设置GPIO模式为BCM编号
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 设置GPIO27为输入模式，上拉模式

while True: # 无限循环
    input_state = GPIO.input(7) # 读取GPIO27的电平状态
    if input_state == False: # 如果电平为低，说明按键被按下
        print('Button Pressed') # 打印输出提示信息
        time.sleep(0.2) # 延时0.2秒，防止抖动