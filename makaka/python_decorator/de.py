#%%
"""

"""
from functools import wraps

def a_new_decorator(a_func):
    """
    装饰器函数
    参数：被修饰的函数名
    返回：被装饰后的函数
    """
    @wraps(a_func)
    def wrapTheFunction():
        print("函数之前运行")
        a_func()
        print("函数之后运行")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("函数运行")

a_function_requiring_decoration()

# %%
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()

#%%

