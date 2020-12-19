import os

def get_files_count(p: str) -> int:
    return len(os.listdir(p))

path = r'C:\Users\MC_VIC\Dropbox\1 семестр\ПИ\лр3'
files_count = get_files_count(path)

print(files_count)