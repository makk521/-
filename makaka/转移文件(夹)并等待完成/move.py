import subprocess

cmd = 'cp -rf /home/pi/pico_file/lib/ /media/pi/CIRCUITPY'

p_lib = subprocess.Popen(cmd, shell=True)
return_lib = p_lib.wait()   #等待子进程结束，并返回状态码；