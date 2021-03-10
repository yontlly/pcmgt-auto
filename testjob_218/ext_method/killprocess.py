import os
import psutil

class KillProcess(object):
    def kill_process(name):
        pids = psutil.pids()
        try:
            for pid in pids:
                p = psutil.Process(pid)
                # print('pid-%s,pname-%s' % (pid, p.name()))
                if p.name() == name:
                    cmd = 'taskkill /F /IM '+name
                    os.system(cmd)
        except:
            pass