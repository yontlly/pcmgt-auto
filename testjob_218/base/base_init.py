import os
import xlrd
import yaml


def dir_base(fileName,filePath='data'):
    return os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),filePath,fileName)

def getYamlData():
    f = open(dir_base('thread.yaml'),'r')
    yaml_data = yaml.safe_load(f)
    return yaml_data

print(type(getYamlData()['threadnum']))
dict=getYamlData()['browsers']
print(getYamlData()['browsers'][0])

for i in range(len(dict)):
    print(dict[i]['host'])
    print(dict[i]['browser'])