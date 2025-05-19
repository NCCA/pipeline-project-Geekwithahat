'''
Folder and layer creation for Big Manager

```
Folder Methods
------------
massRename(string name)
    Mass Formats all new members of a folder by pre-pending name.
    (For formatting folder name)

createFolder(string foldername)
    Creates folder from selection.

createFolderOpen(string foldername)
    Creates folder from selection, unparents objects from pre-existing folders.

find(string regEx, string foldername)
    Creates a folder from objects whose names match the regex function provided.

findOpen(string regEx, string foldername)
    Creates a folder from objects whose names match the regex function provided, unparents objects from pre-existing folders.

conditionalFolder(string condition, string folder)
    Creates a folder from objects that match the given python function.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

conditionalFolderOpen(string condition, string folder)
    Creates a folder from objects that match the given python function, unparents objects from pre-existing folders.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

findConditionFolder(string condition, string folderName)
    Creates a folder from objects that both match the regex function and the given python function.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

findConditionFolderOpen(string condition, string folderName)
    Creates a folder from objects that both match the regex function and the given python function, unparents objects from pre-existing folders.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

cleanFolders()
    Removes folder objects without items within them. Automatically called whenever an Open function is called.

```
Layer Methods
-------------
shiftLayer(string layerName)
    Places current selection into a new display layer.

shiftLayerSearch(string regEx, string layerName)
    Places all objects that match a regEx string into a display layer.

shiftLayerCondition(string condition, string layerName)
    Creates a display layer from objects that match the given python function.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

shiftLayerSearchAndCondition(string condition, string regEx, string layerName)
    Creates a display layer from objects that match the given search condition and provided RegEx function.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

'''


#------ IMPORTS ------

import re
import maya.cmds as cmds

# ------ FOLDER FUNCTIONS ------


# formats items within folder
def massRename(name: str) -> None :
    '''
    Mass Formats all new members of a folder.

    Parameters:
    -----------
    name - Folder name to be prepended to all objects in a folder.

    Process:
    --------
    Gain all names without numbers and alterations ->

    Preppend name of folder ->

    Assign dictionary as { origName : rename } ->

    Reassign names ->

    Allow Maya to handle numbering of repeats (automatic)
    '''

    # prevent previous
    cmds.select(clear=True)

    # select folder
    cmds.select(name, hierarchy = True)

    # save selection
    selected = cmds.ls(selection=True)
    
    # folder name
    assetName = selected[0]
    
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
def createFolder(folderName : str) -> None :
    '''
    Creates folder from selection.

    Parameters:
    -----------
    folderName - Name of folder to be created.
    '''
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
def createFolderOpen(folderName : str) -> None :
    '''
    Creates folder from selection, unparents objects from pre-existing folders.

    Parameters:
    -----------
    folderName - name of folder to be created.
    '''
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


def find(regEx : str, folderName : str) -> None :
    '''
    Creates a folder from objects whose names match the regex function provided.

    Parameters:
    ----------
    regEx - regEx to search names with.
    folderName - name of folder to be created.
    '''
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

def findOpen(regEx : str, folderName : str) -> None :
    '''
    Creates a folder from objects whose names match the regex function provided, unparents objects from pre-existing folders.

    Parameters:
    -----------
    regEx - regEx to search names with.
    folderName - name of folder to be created.
    '''
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

def conditionalFolder(condition : str, folderName : str) -> None :
    '''
    Creates a folder from objects that match the given python function.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

    Parameters:
    -----------
    condition - condition to check for adding item to folder.
    folderName - name of folder to be created.
    '''
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

def conditionalFolderOpen(condition : str, folderName : str) -> None:
    '''
    Creates a folder from objects that match the given python function, unparents objects from pre-existing folders.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

    Parameters:
    -----------
    condition - condition to check for adding item to folder.
    folderName - name of folder to be created.
    '''
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

def findConditionFolder(condition : str, regEx : str, folderName : str) -> None:
    '''
    Creates a folder from objects that both match the regex function and the given python function.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

    Parameters:
    ----------
    condition - condition to check for adding item to folder.
    folderName - name of folder to be created.
    regEx - regEx to search names with.
    '''
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

def findConditionFolderOpen(condition : str, regEx : str, folderName : str) -> None:
    '''
    Creates a folder from objects that both match the regex function and the given python function, unparents objects from pre-existing folders.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

    Parameters:
    ----------
    condition - condition to check for adding item to folder.
    folderName - name of folder to be created.
    regEx - regEx to search names with.
    '''
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

def cleanFolders() -> None:
    '''
    Removes folder objects without items within them. Automatically called whenever an Open function is called.
    '''
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
def shiftLayer(layerName : str) -> None :
    '''
    Places current selection into a new display layer.

    Parameters:
    -----------
    layerName - name 
    '''
    if cmds.ls(selection=True) != [] :
        cmds.createDisplayLayer(name=layerName)
    else:
        cmds.warning("Please alter selection.")

def shiftLayerSearch(regEx : str, layerName : str) -> None :
    '''
    Places all objects that match a regEx string into a display layer.

    Parameters:
    ----------
    regEx - provided regEx string
    layerName - name of layer to create
    '''
    cmds.select(clear=True)
    for i in cmds.ls(typ="transform") :
        if(re.findall(regEx, i) != []):
            cmds.select(i, add=True)
    # create display layer with those that match the condition 
    if cmds.ls(selection=True) != [] :
        cmds.createDisplayLayer(name=layerName)
    else:
        cmds.warning("Please alter selection.")

def shiftLayerCondition(condition : str, layerName : str) -> None :
    '''
    Creates a display layer from objects that match the given python function.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

    Parameters:
    ------------
    condition - condition to check object for to add to display layer
    layerName - name of layer to create
    '''
    cmds.select(clear=True)
    for X in cmds.ls(typ="transform") :
        if(eval(condition)):
            cmds.select(X, add=True)
    if cmds.ls(selection=True) != [] :
        cmds.createDisplayLayer(name=layerName)
    else:
        cmds.warning("Please alter selection.")

def shiftLayerSearchAndCondition(condition : str, regEx : str, layerName : str) -> None :
    '''
    Creates a display layer from objects that match the given search condition and provided RegEx function.
    Mostly useful for Cmds.getAttr() functions.
    Each evaluated function is referered to as X.

    Parameters:
    -----------
    condition - condition to check object for to add to display layer
    layerName - name of layer to create
    regEx - provided regEx string
    '''
    cmds.select(clear=True)
    for X in cmds.ls(typ="transform") :
        if(re.findall(regEx, X) != [] and eval(condition)):
            cmds.select(X, add=True)
    # create display layer with those that match the condition 
    if cmds.ls(selection=True) != [] :
        cmds.createDisplayLayer(name=layerName)
    else:
        cmds.warning("Please alter selection.")
