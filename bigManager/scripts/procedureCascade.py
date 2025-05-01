import maya.cmds as cmds
import os
import re
import maya.mel as mel 


# def createFunctionOut():
#     cmds.scriptEditorInfo(ch=True)
#     streamOut = os.open("stream.txt", os.O_CREAT)
#     cmds.scriptEditorInfo( historyFilename="stream.txt", writeHistory=True )

# def readFunctions():
#     streamOut = os.open("stream.txt", os.O_RDWR)
#     return os.read(streamOut, os.path.getsize("stream.txt")).decode()

# def writeFunctions(Input) :
#     streamOut = os.open("stream.txt", os.O_RDWR)
#     s = Input
#     os.write(streamOut, str.encode(s))

# def deleteFunctions() :
#     os.remove("stream.txt")

def cascadeFunctions(Folder, Code) :
    cmds.select(clear=True)
    Reg = "^"+Folder+"_.*"
    for i in cmds.ls(typ="transform") :
        if(re.findall(Reg, i) != []):
            cmds.select(i, add=True)
    x = cmds.ls(sl=True, typ="transform")


    for object in x :
        cmds.select(object)
        exec(Code)

def repeatLast(Folder) :
    cmds.select(clear=True)
    Reg = "^"+Folder+"_.*"
    for i in cmds.ls(typ="transform") :
        if(re.findall(Reg, i) != []):
            cmds.select(i, add=True)
    x = cmds.ls(sl=True, typ="transform")


    for o in x :
        cmds.select(o)
        print(o)
        mel.eval("RepeatLast")        
    
