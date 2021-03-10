import unittest
import os
import HTMLTestRunner
import time as t

def allTests():
    suite=unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__),'testCase'),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite

def getNowTime():
    return t.strftime('%Y-%m-%d %H_%M_%S',t.localtime(t.time()))

def run():
    filename=os.path.join(os.path.dirname(__file__),'report',getNowTime()+'login.html')
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='报告',
        description='详细报告'
    )
    runner.run(allTests())

if __name__=='__main__':
    run()