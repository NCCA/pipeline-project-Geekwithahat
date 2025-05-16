'''
Folder and layer creation for Big Manager
'''


#------ IMPORTS ------

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
    
    for f in range(len(selected)):

        if(re.findall("^.*?_", selected[f]) != None and ('Shape' not in selected[f])):
            cmds.select(selected[f])
            cmds.rename(re.sub("^.*?_","",selected[f]))
            selected[f] = re.sub("^.*?_","",selected[f])
        
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
    if(re.search('[a-zA-Z]', folderName)) :
        # existence check
        if(cmds.ls(selection=True) != []):
            # save selection
            selection = cmds.ls(selection=True)
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
    else:
        cmds.warning("Please provide letter characters to name.")

# create folder with reorganisation
def createFolderOpen(folderName) -> None :
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        # check if in folder
        select = cmds.ls(selection=True)
        if(select != []):
            # remove from folder if in folder
            for i in select:
                try:
                    if(cmds.getAttr(cmds.listRelatives(parent=True)[0] + ".FolderFlag")):
                        cmds.parent(world=True)
                except:
                    continue
            cmds.select(select)
            cmds.group(n=folderName)
            # folder identifier
            cmds.addAttr(folderName, longName="FolderFlag", attributeType="bool", defaultValue=True)
            massRename(folderName)
            cleanFolders()
        else:
            cmds.warning("Please alter selection of objects")
    else:
        cmds.warning("Please provide a unique folder name")


def find(regEx, folderName) -> None :
    # check name
    if(folderName != "" and cmds.ls(folderName) != [folderName]): 
        # clear previous selection 
        cmds.select(clear=True)
        # check all valid objects  
        for i in cmds.ls(typ="transform") :
            # run regex on name
            if(re.findall(regEx, i) != []):
                cmds.select(i, add=True)
        # add matches to folder
        createFolder(folderName) 
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name")

def findOpen(regEx, folderName) -> None :
    # check name
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        selection = []
        for i in cmds.ls(typ="transform") :
            if(re.findall(regEx, i) != []):
                # remove existing folders
                parent = cmds.listRelatives(i, parent=True)
                if(parent != None):
                    # fetch parent
                    parent = parent[0]
                    # check parent is a folder (error if not found hence try)
                    try:
                        if(cmds.getAttr(parent + ".FolderFlag")):
                            cmds.parent(i,world=True)
                    except:
                        pass
                cmds.select(i)
                selection += cmds.ls(selection=True)
        cmds.select(selection)
        createFolder(folderName)
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name")

def conditionalFolder(condition, folderName) -> None :
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        for X in cmds.ls(typ="transform") :
            # run condition as python code to evaluate
            if(eval(condition)):
                cmds.select(X, add=True)
        createFolder(folderName) 
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name")

def conditionalFolderOpen(condition, folderName) -> None:
    # repeat open command with condition evaluation
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        selection = []
        for X in cmds.ls(typ="transform") :
            if(eval(condition)):
                parent = cmds.listRelatives(X, parent=True)
                if(parent != None):
                    parent = parent[0]
                    try:
                        if(cmds.getAttr(parent + ".FolderFlag")):
                            cmds.parent(X,world=True)
                    except:
                        pass 
                cmds.select(X)
                selection += cmds.ls(selection=True)
        cmds.select(selection)
        createFolder(folderName)
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name") 

def findConditionFolder(condition, regEx, folderName) -> None:
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        for X in cmds.ls(typ="transform") :
            # combine regex with condition
            if(re.findall(regEx, X) != [] and eval(condition)):
                cmds.select(X, add=True)

        createFolder(folderName)
        cleanFolders()
    else:
        cmds.warning("Please provide a unique folder name") 

def findConditionFolderOpen(condition, regEx, folderName) -> None:
    # same but open
    if(folderName != "" and cmds.ls(folderName) != [folderName]):
        cmds.select(clear=True)
        selection = []
        for X in cmds.ls(typ="transform") : 
            if(re.findall(regEx, X) != [] and eval(condition)):
                try:
                    parent = cmds.listRelatives(X, parent=True)
                    if(parent != None):
                        if(cmds.getAttr(parent + ".FolderFlag")):
                            cmds.parent(X,world=True)
                except:
                    pass
                cmds.select(X)
                selection += cmds.ls(selection=True)
        cmds.select(selection)
        createFolder(folderName)
        cleanFolders()

    else:
        cmds.warning("Please provide a unique folder name") 

def cleanFolders() :
    # get all items in hierarchy
    allTransforms = cmds.ls(typ="transform")
    for i in allTransforms : 
        try:
            # check if both a folder and empty -> remove
            if cmds.listRelatives(i, children=True) == None and cmds.getAttr(i + ".FolderFlag") :
                cmds.delete(i)
        except:
            pass


# ------ SHIFT LAYER ------

# similar functionality for layers
def shiftLayer(layerName) -> None :
    if cmds.ls(selection=True) != [] :
        cmds.createDisplayLayer(name=layerName)
    else:
        cmds.warning("Please alter selection.")

def shiftLayerSearch(regEx, layerName) -> None :
    cmds.select(clear=True)
    for i in cmds.ls(typ="transform") :
        if(re.findall(regEx, i) != []):
            cmds.select(i, add=True)
    # create display layer with those that match the condition 
    if cmds.ls(selection=True) != [] :
        cmds.createDisplayLayer(name=layerName)
    else:
        cmds.warning("Please alter selection.")

def shiftLayerCondition(condition, layerName) -> None :
    cmds.select(clear=True)
    for X in cmds.ls(typ="transform") :
        if(eval(condition)):
            cmds.select(X, add=True)
    if cmds.ls(selection=True) != [] :
        cmds.createDisplayLayer(name=layerName)
    else:
        cmds.warning("Please alter selection.")

def shiftLayerSearchAndCondition(condition, regEx, layerName) -> None :
    cmds.select(clear=True)
    for X in cmds.ls(typ="transform") :
        if(re.findall(regEx, X) != [] and eval(condition)):
            cmds.select(X, add=True)
    # create display layer with those that match the condition 
    if cmds.ls(selection=True) != [] :
        cmds.createDisplayLayer(name=layerName)
    else:
        cmds.warning("Please alter selection.")
