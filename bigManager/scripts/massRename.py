#import maya.standalone
#maya.standalone.initialize(name="python")

import re
import maya.cmds as cmds

def massRename(name) -> None :
    cmds.select(clear=True)
    cmds.select(name, hierarchy = True)
    selected = cmds.ls(selection=True)
    
    assetName = selected[0]
    
    replace = {}
    
    for c in selected :
         cN = re.findall("[A-Z, a-z 0-9, ^|_]*[a-z, A-Z]", c)[0]
         if (cN == assetName) | ("|" in cN) | (re.search(".*Shape", cN) != None) | (c in replace):
             continue
         replace[c] = assetName + "_" + cN
    
    
    for rn in selected : 
        if (rn == assetName) | ('|' in rn) | ("Shape" in rn) :
            continue
        cmds.select(rn)
        cmds.rename(replace[rn])


def createFolder(folderName) -> None :
    cmds.group(n=folderName)
    massRename(folderName)

def find(regEx, folderName) -> None :
    cmds.select(clear=True)
    for i in cmds.ls(typ="transform") :
        if(re.findall(regEx, i) != []):
            cmds.select(i, add=True)

    createFolder(folderName) 

def findOpen(regEx, folderName) -> None :
    cmds.select(clear=True)
    for i in cmds.ls(typ="transform") :
        if(re.findall(regEx, i) != []):
            cmds.Unparent()
            cmds.select(i, add=True)

    createFolder(folderName) 

def shiftLayer(regEx, layerName) -> None :
    cmds.select(clear=True)
    for i in cmds.ls(typ="transform") :
        if(re.findall(regEx, i) != []):
            cmds.select(i, add=True)
    cmds.createDisplayLayer(name=layerName)

def conditionalFolder(condition, folderName) :
    cmds.select(clear=True)
    for X in cmds.ls(typ="transform") :
        print(condition)
        if(eval(condition)):
            cmds.select(X, add=True)
    createFolder(folderName) 

def conditionalFolderOpen(condition, folderName) :
    cmds.select(clear=True)
    for X in cmds.ls(typ="transform") :
        if(eval(condition)):
            cmds.Unparent()
            cmds.select(X, add=True)
    createFolder(folderName) 

    