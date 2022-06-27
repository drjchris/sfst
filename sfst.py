from genericpath import isdir
from json import loads, dumps
from os.path import isdir
from os import makedirs
from os import listdir
from xmlrpc.client import Boolean

from datetime import datetime

# # json i/o files
def readJson(filepath:str) -> dict:
    with open(filepath, 'r') as fr:
        outdict = loads(fr.read())
    return outdict

def writeJson(jdata: dict, filepath:str, indent=None) -> None:
    with open(filepath, 'w') as fw:
        fw.write(dumps(jdata, indent=indent, ensure_ascii=False))
    pass

def printJson(jdata: dict) -> str:
    return json.dumps(jdata, indent=2, ensure_ascii=False)

def checkMake(dirpath: str) -> Boolean:
    if isdir(dirpath)==True:
        pass
        return True
    if isdir(dirpath)==False:
        makedirs(dirpath)
        return False

# lists all files in a dir and removes hidden ones
def listFiles(dirpath: str) -> list:
    return [x for x in listdir(dirpath) if x[0]!='.']

def dtNow():
    return datetime.now().strftime("%Y%m%d%H%M%S")
