'''
Folder and layer creation for Big Manager
'''


#------ IMPORTS ------

#import maya.standalone
#maya.standalone.initialize(name="python")

import re
import maya.cmds as cmds

# ------ FOLDER FUNCTIONS ------


# formats items within folder
def massRename(name) -> None :
    # prevent previous
    cmds.select(clear=True)

    # select folder
    cmds.select(name, hierarchy = True)

    # save selection
    selected = cmds.ls(selection=True)
    
    # folder name
    assetName = selected[0]
    
    '''
    Gain all names without numbers and alterations ->
    Preppend name of folder ->
    Assign dictionary as { origName : rename } ->
    Reassign ->
    Allow Maya to handle numbering of repeats (automatic)
    '''
    replace = {}
    
    for c in selected :
         cN = re.findall("[A-Z, a-z 0-9, ^|_]*[a-z, A-Z]", c)[0]
         if (cN == assetName) | ("|" in cN) | (re.search(".*Shape", cN) != None) | (c in replace):
             continue
         replace[c] = assetName + "_" + cN
    
    
    for rn in selected : 
        try:
            if (rn == assetName) | ('|' in rn) | ("Shape" in rn) :
                continue
            cmds.select(rn)
            cmds.rename(replace[rn])
        except:
            continue

# basic selection folder
def createFolder(folderName) -> None :
    # existence check
    if(cmds.ls(selection=True) != []):
        # name check 
        if(folderName != "" and cmds.ls(folderName) != [folderName]):

            cmds.group(n=folderName)
            cmds.addAttr(folderName, longName="FolderFlag", attributeType="bool", defaultValue=True)
            massRename(folderName)
            cleanFolders()
        else:
            cmds.warning("Please provide a unique folder name")
    else:
        cmds.warning("Please alter selection of objects")

# create folder with reorganisation
def createFolderOpen(folderName) -> None :
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        # check if in folder
        select = cmds.ls(selection=True)
        for i in select:
            try:
                if(cmds.getAttr(cmds.listRelatives(parent=True)[0] + ".folderFlag")):
                    cmds.parent(world=True)
            except:
                continue
        cmds.select(select)
        cmds.group(n=folderName)
        massRename(folderName)
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name")


def find(regEx, folderName) -> None :
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        for i in cmds.ls(typ="transform") :
            if(re.findall(regEx, i) != []):
                cmds.select(i, add=True)
        createFolder(folderName) 
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name")

def findOpen(regEx, folderName) -> None :
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        selection = []
        for i in cmds.ls(typ="transform") :
            if i == folderName :
                selfFlag = 1 
            if(re.findall(regEx, i) != []):
                parent = cmds.listRelatives(i, parent=True)
                if(parent != None):
                    parent = parent[0]
                    try:
                        if(cmds.getAttr(parent + ".folderFlag")):
                            cmds.parent(i,world=True)
                    except:
                        continue
                cmds.select(i)
                selection += cmds.ls(selection=True)
        cmds.select(selection)
        createFolder(folderName)
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name")

def conditionalFolder(condition, folderName) :
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        for X in cmds.ls(typ="transform") :
            if(eval(condition)):
                cmds.select(X, add=True)
        createFolder(folderName) 
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name")

def conditionalFolderOpen(condition, folderName) :
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        for X in cmds.ls(typ="transform") :
            if(eval(condition)):
                if(bool(cmds.listRelatives(i, parent=True))):
                    cmds.parent(X,world=True)
                cmds.select(X, add=True)
        createFolder(folderName)
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name") 

def findConditionFolder(condition, regEx, folderName):
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        for X in cmds.ls(typ="transform") :
            if(re.findall(regEx, X) != [] and eval(condition)):
                cmds.select(X, add=True)

        createFolder(folderName)
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name") 

def findConditionFolderOpen(condition, regEx, folderName):
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        for X in cmds.ls(typ="transform") : 
            if(re.findall(regEx, X) != [] and eval(condition)):
                if(bool(cmds.listRelatives(i, parent=True))):
                    cmds.parent(X,world=True)
                cmds.select(X, add=True)

        createFolder(folderName)
        cleanFolders()

    else:
        cmds.warning("Please provide a unique folder name") 

def cleanFolders() :
    allTransforms = cmds.ls(typ="transform")
    for i in allTransforms : 
        if cmds.listRelatives(i) == None :
            cmds.delete(i)



def shiftLayer(regEx, layerName) -> None :
    cmds.select(clear=True)
    for i in cmds.ls(typ="transform") :
        if(re.findall(regEx, i) != []):
            cmds.select(i, add=True)
    cmds.createDisplayLayer(name=layerName)