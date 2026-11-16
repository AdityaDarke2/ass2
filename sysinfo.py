import os


hw_model = os.popen("cat /sys/devices/virtual/dmi/id/product_name 2>/dev/null").read().strip()
memory = os.popen("free -h | awk '/Mem:/ {print $2}'").read().strip()
processor = os.popen("lscpu | grep 'Model name' | cut -d':' -f2 | xargs").read().strip()
cache_size = os.popen("grep -m 1 'cache size' /proc/cpuinfo | cut -d':' -f2 | xargs").read().strip()
graphics = os.popen("lspci | grep -iE 'VGA|3D' | cut -d':' -f3- | xargs").read().strip()
disk_cap = os.popen("df -h --total | awk '/total/ {print $2}'").read().strip()
os_name = os.popen("grep PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d '\"'").read().strip()


gnome_ver = os.popen("xfce4-session --version").read().strip()
kernel_ver = os.popen("uname -r").read().strip()
hostname = os.popen("hostname").read().strip()
os_type = os.popen("getconf LONG_BIT").read().strip() + "-bit"
win_system = os.environ.get("XDG_SESSION_TYPE", "Unknown")


print("<-----Hardware Information----->")
print("Hardware Model: " + hw_model)
print("Memory: " + memory)
print("Processor: " + processor)
print("Cache Size: " + cache_size)
print("Graphics: " + graphics)
print("Disk Capacity: " + disk_cap)
print("")


print("<-----Software Information----->")
print("OS Name: " + os_name)
print("GNOME Version: " + gnome_ver)
print("Kernel Version: " + kernel_ver)
print("Hostname: " + hostname)
print("OS Type: " + os_type)
print("Windowing System: " + win_system)
