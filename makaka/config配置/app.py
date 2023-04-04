'''
pip install pyyaml
'''
import yaml

with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

print(config)
print(type(config['api_url']))
