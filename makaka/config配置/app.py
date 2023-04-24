# %%
'''
返回一个字典,key为字符串
'''
import yaml
with open("config.yaml", "r") as f:
    CONFIG = yaml.load(f, Loader=yaml.FullLoader)
print(CONFIG)
print(type(CONFIG['api_url']))