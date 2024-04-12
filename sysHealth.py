import psutil
import logging

# Setup logging
logging.basicConfig(filename="system_health.log", level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(message)s')

CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 80  

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    else:
        print(f"CPU Usage: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = (memory.used / memory.total) * 100
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage:.2f}%")
    else:
        print(f"Memory Usage: {memory_usage:.2f}%")

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = (disk.used / disk.total) * 100
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {disk_usage:.2f}%")
    else:
        print(f"Disk Usage: {disk_usage:.2f}%")

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()

if __name__ == "__main__":
    main()
