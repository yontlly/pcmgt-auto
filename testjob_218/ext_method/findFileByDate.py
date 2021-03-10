import os
import fnmatch
import datetime


class FindFileByDate(object):
    def find_file(self,file_path):

        files = []
        for dirpath,dirnames,file in os.walk(file_path):
            files = file

        filesize = {}
        for file in files:
            if os.stat(file_path+file).st_size > 0:
                if fnmatch.fnmatch(str(file), '*.*'):
                    time = datetime.datetime.fromtimestamp(os.stat(file_path + file).st_mtime)
                    filesize.update({file: time})

        return file_path+max(filesize, key=filesize.get)
