import os
import fnmatch
import datetime
files=[]

#file_path=r"C:/android_file/"
#file_path=r"C:/pc_file/"
file_path=r"C:/ios_file/"
for dirpath,dirnames,file in os.walk(file_path):
    files = file

filesize={}
for file in files:
    if os.stat(file_path+file).st_size > 0:
        if fnmatch.fnmatch(str(file),'*.*'):
            time =datetime.datetime.fromtimestamp(os.stat(file_path+file).st_mtime)
            filesize.update({file:time})

print(filesize)

print(file_path+max(filesize, key=filesize.get))

