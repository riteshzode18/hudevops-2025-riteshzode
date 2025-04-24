import os
import psutil
import json


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


if __name__ == '__main__':
    data = {
        "memory_info": get_memory_info(),
        "cpu_info": get_cpu_info(),
        "disk_info": get_disk_info(),
    }
    print("="*40)
    print("System Monitoring")
    print("="*40)
    print(json.dumps(data, indent=4))
    