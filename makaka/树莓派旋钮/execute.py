'''                 __         __        
   ____ ___  ____ _/ /______ _/ /______ _
  / __ `__ \/ __ `/ //_/ __ `/ //_/ __ `/
 / / / / / / /_/ / ,< / /_/ / ,< / /_/ / 
/_/ /_/ /_/\__,_/_/|_|\__,_/_/|_|\__,_/ 

按钮简单使用
参考:
    https://gist.github.com/brucesdad13/4ac8ceeb904903b9346fc1fa4d579c73
    https://gpiozero.readthedocs.io/en/stable/api_input.html#rotaryencoder
除此之外还有按键检测
'''
from gpiozero import RotaryEncoder

# 定义旋钮对象，BCM编码 
encoder = RotaryEncoder(27, 23)

# 定义旋转方向的回调函数
def shun(data):
    print(data)

def ni():
    print('逆时针')


if __name__ == '__main__':
    encoder.when_rotated_clockwise = lambda: shun('顺时针')
    encoder.when_rotated_counter_clockwise = ni
    while True:
        pass
