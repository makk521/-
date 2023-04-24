'''
Simultaneously transmit two pieces of data to the cloud through two ports
'''
import socket
import sys
import time
from threading import Thread
from sensor import SHT20
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
LED = 27
FUN = 26
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(FUN, GPIO.OUT)
BUTTON_LED = 17                   # 后期换成传感器
GPIO.setup(BUTTON_LED, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # 引脚默认高电平（拉高），按下后接地引脚电平被拉低
GPIO.output(LED,GPIO.LOW)

def sock_client_data(address,send_data):
    """
    Connect to cloud and send data(every three seconds)

    Arguments:
    address    - ('cloud public mac', port)
    send_data  
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))

    while True:
        s.send(send_data.encode('utf-8'))  # 将要传输的数据编码发送，如果是字符数据就必须要编码发送
        time.sleep(3)

def send_data_background(addr,delay_time):
    """
    Send furniture status and sensor data

    Arguments:
    addr         -  ('cloud_public_mac', PORT)
    delay_time   -  seconds between sending

    Plus:
    data structure - str((led_status , fun_status , temperature , humidity))
    """
    try:
        soc_bg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc_bg.connect(addr)
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))
    sht = SHT20(1, 0x40)
    while(True):
        led_status   =  GPIO.input(LED) # 0/1
        fun_status   =  GPIO.input(FUN)
        temperature  =  sht.temperature().C
        humidity     =  sht.humidity().RH
        data = str((led_status , fun_status , temperature , humidity))
        soc_bg.send(data.encode('utf-8'))
        time.sleep(delay_time)

# 回调函数，按下按键的中断执行函数，现象为灯亮起且发送两次数据给云端
def led_button_callback(BUTTON_LED):
    """
    When the button is pressed, the current state of the LED is changed and the information is sent to the cloud
    """
    print('按键按下')
    if GPIO.input(LED) == 0:
        GPIO.output(LED,GPIO.HIGH)
    else:
        GPIO.output(LED,GPIO.LOW)




GPIO.add_event_detect(BUTTON_LED, GPIO.RISING, callback=led_button_callback, bouncetime=400)    # 检测BUTTON_LED的中断函数

if __name__ == '__main__':
    ADDR1 = ('124.223.76.58', 7789)
    ADDR2 = ('124.223.76.58', 8081)

    Thread(target = sock_client_data,args=(ADDR1,"a")).start()
    Thread(target = send_data_background,args=(ADDR2,3)).start()

