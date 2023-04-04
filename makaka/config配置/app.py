'''
pip install pyyaml
'''
import yaml

with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

<<<<<<< HEAD
print(config[key])
=======
print(config)
>>>>>>> 5cb771141d74256fbabca350bb961a8ed65c8746
