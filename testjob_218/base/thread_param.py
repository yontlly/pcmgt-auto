from threading import Thread
from utils.operationData import *
from pytest_test import *

def thread_browser(func):

    lists = {
        'http://192.168.44.1:4444/wd/hub': 'chrome',
        'http://192.168.44.1:6665/wd/hub': 'firefox',
        'http://192.168.44.134:6666/wd/hub': 'chrome'  # 远程节点
    }
    threads = []
    files = range(len(lists))
    # 创建线程
    for host, browser in lists.items():
        t = Thread(target=func, args=(host, browser))
        threads.append(t)
    '''
    threads = []
    files=OperationData.getYamlData()['threadnum']
    # 创建线程
    for i in range(files):
        t = Thread(target=func)
        threads.append(t)
    '''
    # 启动线程
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()