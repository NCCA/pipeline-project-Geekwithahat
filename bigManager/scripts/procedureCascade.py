import maya.cmds as cmds
import os
import re


def createFunctionOut():
    cmds.scriptEditorInfo(ch=True)
    streamOut = os.open("stream.txt", os.O_CREAT)
    cmds.scriptEditorInfo( historyFilename="stream.txt", writeHistory=True )

def readFunctions():
    streamOut = os.open("stream.txt", os.O_RDWR)
    return os.read(streamOut, os.path.getsize("stream.txt")).decode()

def writeFunctions(Input) :
    streamOut = os.open("stream.txt", os.O_RDWR)
    s = Input
    os.write(streamOut, str.encode(s))

def deleteFunctions() :
    os.remove("stream.txt")

def cascadeFunctions(Folder, Code) :
    for i in cmds.ls(typ="transform") :
        if(re.findall(Folder, i) != []):
            cmds.select(i, add=True)
    cmds.select(Folder,d=True)
    x = cmds.ls(sl=True, typ="transform")


    for object in x :
        cmds.select(object)
        exec(Code)
    
