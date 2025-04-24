import json 
import yaml 
import psutil 
import requests 
from bs4 import BeautifulSoup


json_file = "main.json"
yaml_file = "main.yaml"

print("Json file read")
with open(json_file, mode="r") as f:
    try:
        json_data = json.load(f)
        # print(json_data, end="\n")
    except Exception as e:
        print(f"Error {e}")    


print("Yaml file read")
with open(yaml_file, mode="r") as f:
    try:
        yaml_data = yaml.safe_load(f)  
        # print(yaml_data)
    except Exception as e:
        print(f"Error reading YAML file: {e}")      


print("Current system specifications")

def get_cpu_info():
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "processor_speed": psutil.cpu_freq().current,
        "cpu_usage_per_core": dict(enumerate(psutil.cpu_percent(percpu=True, interval=1))),
        "total_cpu_usage": psutil.cpu_percent(interval=1)
    }


def get_memory_info():
    return {
        "total_memory": psutil.virtual_memory().total / (1024.0 ** 3),
        "available_memory": psutil.virtual_memory().available / (1024.0 ** 3),
        "used_memory": psutil.virtual_memory().used / (1024.0 ** 3),
        "memory_percentage": psutil.virtual_memory().percent
    }


def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.mountpoint] = {
            "total_space": partition_usage.total / (1024.0 ** 3),
            "used_space": partition_usage.used / (1024.0 ** 3),
            "free_space": partition_usage.free / (1024.0 ** 3),
            "usage_percentage": partition_usage.percent
        }
    return disk_info

system_data = {
        "memory_info": get_memory_info(),
        "cpu_info": get_cpu_info(),
        "disk_info": get_disk_info(),
    }

print("Scraped data from the website")

from bs4 import BeautifulSoup
import requests

# Fetch the HTML content from the Python website
url = "https://www.python.org/"

r = requests.get(url)
data = r.text
print(f"HTTP  status code : {r.status_code}")

soup = BeautifulSoup(data, 'html.parser')

# Print prettified HTML to the console
# print(soup.prettify())

# with open("file.html", mode="w", encoding="utf-8") as f:
#     f.write(soup.prettify())


print(f"Title : {soup.title.text}")

# heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
heading_tags = ["h1", "h2"]

for heading in heading_tags:
    print(f"ALL {heading} HEADINGS")
    for text in soup.find_all(heading):
        print(text.text.strip())
    print()    
        

scraped_data = {
    'url': url,
    'status_code': r.status_code,
    'title': soup.title.string if soup.title else 'No title found',
}        


combined_output = {
    'json_file_data': json_data,
    'yaml_file_data': yaml_data,
    'system_health': system_data,
    'scraped_website_data': scraped_data
}

# --- Output JSON to file ---
with open('combined_output.json', 'w') as outfile:
    json.dump(combined_output, outfile, indent=2)

# Print to console
print(json.dumps(combined_output, indent=2))



