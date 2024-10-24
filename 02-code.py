import os
import platform

def display_system_info():
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

def display_working_directory():
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")
    return cwd

def list_files_and_directories(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(f"File: {entry.name}")
            elif entry.is_dir():
                print(f"Directory: {entry.name}")

display_system_info()
cwd = display_working_directory()
list_files_and_directories(cwd)



