#import maya.standalone
#maya.standalone.initialize(name="python")

import re
import maya.cmds as cmds

def massRename(name) -> None :
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
        if (rn == assetName) | ('|' in rn) | ("Shape" in rn) | (assetName in rn):
            continue
        cmds.select(rn)
        cmds.rename(replace[rn])


def createFolder(folderName) -> None :
    cmds.group(n=folderName)
    massRename(folderName)

def find(regEx, folderName) -> None :
    for i in cmds.ls(typ="transform") :
        if(re.findall(regEx, i) != []):
            cmds.select(i, add=True)

    createFolder(folderName)     
   

#createFolder("A")
    