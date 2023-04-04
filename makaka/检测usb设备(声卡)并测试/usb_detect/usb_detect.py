'''
识别usb设备并做出反应。
sink_name_lsusb ----> usb声卡名称(lsusb指令)
sink_name_pacmd ----> usb声卡名称(pacmd指令)
test_mp3_path   ----> 播放的测试音频地址
usb_name_lsusb  ----> usb测试设备名称(lsusb指令)
'''
import subprocess
import yaml
import re
import vlc
import time
from threading import Thread

class USB_DETECT:
    CONFIG = None
    
    def __init__(self):
        '''
        导入config并开始播放测试音频。
        '''
        with open("config.yaml", "r") as f:
            CONFIG = yaml.load(f, Loader=yaml.FullLoader)
        self.sink_name_lsusb = CONFIG['sink_name_lsusb'] 
        self.sink_name_pacmd = CONFIG['sink_name_pacmd']
        self.test_mp3_path = CONFIG['test_mp3_path']
        self.usb_name_lsusb = CONFIG['usb_name_lsusb']
        self.SINK_DETECT_STATUS = False
        self.USB_DETECT_STATUS = False
        self.play_audio = vlc.MediaPlayer(self.test_mp3_path)
        self.play_audio.play()
        
        pass

    def usb_sink_detect(self): 
        '''
        不断查询声卡名称是否存在于当前插入的usb设备中。若第一次插入则切换其为默认声卡。
        '''
        while True:    
            output = str(subprocess.check_output('lsusb',shell=True).decode('utf-8'))
            result = len(re.findall(self.sink_name_lsusb,output))
            if(result != 0 and self.SINK_DETECT_STATUS == False):
                self.SINK_DETECT_STATUS = True
                time.sleep(1)
                subprocess.call(f'pacmd set-default-sink {self.sink_name_pacmd}',shell = True)
                print('sink has detected')
            elif(result != 0 and self.SINK_DETECT_STATUS == True):
                pass
            elif(result == 0 and self.SINK_DETECT_STATUS == True):
                self.SINK_DETECT_STATUS = False
                print('sink been plugged out')
            else:
                pass
            
    def usb_usb_detect(self):
        '''
        不断查询测试usb设备是否存在于当前插入的usb设备中。
        '''
        while True:
            output = str(subprocess.check_output('lsusb',shell=True).decode('utf-8'))
            result = len(re.findall(self.usb_name_lsusb,output))
            if(result != 0 and self.USB_DETECT_STATUS == False):
                self.USB_DETECT_STATUS = True
                print('usb has detected')
            elif(result != 0 and self.USB_DETECT_STATUS == True):
                pass
            elif(result == 0 and self.USB_DETECT_STATUS == True):
                self.USB_DETECT_STATUS = False
                print('usb been plugged out')
            else:
                pass

if __name__ == "__main__":
    my_detect = USB_DETECT()
    Thread(target = my_detect.usb_sink_detect).start()
    Thread(target = my_detect.usb_usb_detect).start()

