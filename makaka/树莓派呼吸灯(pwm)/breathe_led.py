'''
pwm控制呼吸灯
'''
import RPi.GPIO as GPIO
import time

LED1 = 5
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BCM)		#set pin numbering system
GPIO.setup(LED1,GPIO.OUT)

def breathe_led(LED):
    pi_pwm = GPIO.PWM(LED,1000)
    pi_pwm.start(0)
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        time.sleep(0.01)
    for duty in range(100,-1,-1):
        pi_pwm.ChangeDutyCycle(duty)
        time.sleep(0.01)

if __name__ == '__main__':
    breathe_led(LED1)