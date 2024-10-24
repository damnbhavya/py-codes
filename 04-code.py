import os
import time

file_path = r'C:\Users\Bhavya\OneDrive\codes\py-codes\04-code.py'

file_mode = os.stat(file_path).st_mode
print(f"File mode: {file_mode}")

access_time = os.path.getatime(file_path)
modify_time = os.path.getmtime(file_path)
change_time = os.path.getctime(file_path)

lat = time.localtime(access_time)
lmt = time.localtime(modify_time)
lct = time.localtime(change_time)

gat = time.gmtime(access_time)
gmt = time.gmtime(modify_time)
gct = time.gmtime(change_time)

print("Local Access Time:", time.strftime("%Y-%m-%d %H:%M:%S", lat))
print("Local Modify Time:", time.strftime("%Y-%m-%d %H:%M:%S", lmt))
print("Local Change Time:", time.strftime("%Y-%m-%d %H:%M:%S", lct))

print("GMT Access Time:", time.strftime("%Y-%m-%d %H:%M:%S", gat))
print("GMT Modify Time:", time.strftime("%Y-%m-%d %H:%M:%S", gmt))
print("GMT Change Time:", time.strftime("%Y-%m-%d %H:%M:%S", gct))


