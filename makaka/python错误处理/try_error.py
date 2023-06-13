"""
try-except应用
"""
# %%

try:
    # 可能会引发异常的代码
    pass
except ExceptionType1:
    # 处理异常类型1的代码
    pass
except ExceptionType2:
    pass
    # 处理异常类型2的代码
except:
    # 处理其他异常的代码

# %%

try:
    # 可能会引发异常的代码
    pass
except ExceptionType:
    pass
    # 处理异常的代码    
finally:
    # 无论是否发生异常，都会执行的代码

# %%

try:
except Exception:
    print(Exception)
