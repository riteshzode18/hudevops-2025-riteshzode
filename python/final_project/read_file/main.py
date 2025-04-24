import json
# pip install simplejson

print("Json file read")
with open("main.json", mode="r") as f:
    try:
        data = json.load(f)
        print(data, end="\n")
    except Exception as e:
        print(f"Error {e}")    


import yaml
# pip install pyyaml

print("Yaml file read")
with open("main.yaml", mode="r") as f:
    try:
        data = yaml.safe_load(f)  
        print(data)
    except Exception as e:
        print(f"Error reading YAML file: {e}")        