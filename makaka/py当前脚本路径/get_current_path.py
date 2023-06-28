import os

# 获取当前脚本的路径
script_path = os.path.realpath(__file__)

# 获取当前脚本所在的目录
script_directory = os.path.dirname(script_path)

print(script_path)
print(script_directory)