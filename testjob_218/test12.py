from enum import Enum

class TacticsClient(Enum):
    windows = win = pc = 桌面端 = 桌面 = ['Windows']
    mac = ['Mac']
    android = ['Android']
    ios = ['iOS']
    web = ['Web']
    移动端 = 移动 = ['Android','iOS']

print(TacticsClient['移动端'.lower()].value)

a=['桌面端','移动']
b=[]
for i in a:
    b+=TacticsClient[i.lower()].value

print(b)

a='桌面端'
a=a.split(',')
print(a)

