import psutil

def cpu_check():
    cpu = int(input("Enter the CPU threshold"))
    cpu_thr = psutil.cpu_percent(interval=1)
    
    if cpu_thr > cpu:
        print(f"CPU ALERT :- Current CPU % {cpu_thr}%")
    else:
        print("CPU is in safe state")
    
def disk_check():
    disk = int(input("Enter the Disk threshold"))
    disk_use = psutil.disk_usage('/').percent
    
    if disk_use > disk:
        print("Your disk is about to full : ", disk_use)
    else:
        print("You have enough storage")
    
def memory_check():
    memory = int(input("Enter the Memory threshold"))
    mem = psutil.virtual_memory().percent
    
    if mem > memory:
        print(f"Your current memory is {mem}%")
    else:
        print("You have enough memory")
        
def system_check():
    cpu_check()
    disk_check()
    memory_check()
    
system_check()
