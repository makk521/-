import subprocess
code = '1111'

command = f'echo {code} | mail -s {code} maqun2019@qq.com'
subprocess.run(command,shell = True)