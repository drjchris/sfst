from genericpath import isdir
from json import loads, dumps
from os.path import isdir
from os import makedirs
from xmlrpc.client import Boolean

# # json i/o files
def openJson(filepath:str) -> dict:
    with open(filepath, 'r') as fr:
        outdict = loads(fr.read())
    return outdict

def saveJson(jdata: dict, filepath:str) -> None:
    with open(filepath, 'w') as fw:
        fw.write(dumps(jdata, indent=2, ensure_ascii=False))
    pass

def checkMake(dirpath: str) -> Boolean:
    if isdir(dirpath)==True:
        pass
        return True
    if isdir(dirpath)==False:
        makedirs(dirpath)
        return False