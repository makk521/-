'''                 __         __        
   ____ ___  ____ _/ /______ _/ /______ _
  / __ `__ \/ __ `/ //_/ __ `/ //_/ __ `/
 / / / / / / /_/ / ,< / /_/ / ,< / /_/ / 
/_/ /_/ /_/\__,_/_/|_|\__,_/_/|_|\__,_/ 

环境配置:
    pip install pyfiglet
在线生成:
    http://patorjk.com/software/taag/#p=display&f=Big&t=makaka
'''
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('makaka'))
