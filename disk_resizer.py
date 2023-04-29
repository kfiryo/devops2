from os import getenv


def disk_resizer(disk_name1, machine_name1, target_gb1):
    print("details " + disk_name1 + " " + machine_name1 + " to " + target_gb1)
    print("connecting to vSphere")
    print("locating machine")
    print("resizing disk")
    print("ssh'ing ext4")


disk_name = getenv("DISK_NAME")
machine_name = getenv("MACHINE_NAME")
target_gb = getenv("TARGET_GB")
disk_resizer(disk_name, machine_name, target_gb)
