'''
UI creation in the basic Maya user interface library

todo: eventually convert to Qt?
'''

# ------IMPORTS------

import maya.cmds as cmds
import massRename
import procedureCascade
import webbrowser as wb


# ------GLOBAL VARIABLES------

folderName = "none"

attributesText_F = {}
C = []

attributesText_L = {}
L = []

# Remove existing UI if re-opened.
if cmds.dockControl("bigUI",exists=True) :
    try:
        cmds.deleteUI("bigUI")
        cmds.deleteUI("SL")
        cmds.deleteUI("columnLayout")
    except:
        pass


# ------ATTRIBUTE IDENTIFICATION AND DISPLAY------


def updateSelectedAttributesFolder():
    #import
    global C
    # get shared attributes between selected objects
    for I in cmds.ls(sl=True) :
        A = cmds.listAttr(I, write=True)
        if C == [] :
            C = A
        else :
            C = set(C).intersection(A)
    # sort for ease of traversal
    C = sorted(C)
    updateSelectedAttributeUI_Folder()



def updateSelectedAttributeUI_Folder():
    global C
    for i in C :
        # remove attributes that "don't exist" but still apear (???)
        if "." not in i :
            attributesText_F[i] = cmds.textFieldGrp(i + "_aFF",label=i, parent="attributeColumn_F")

def clearSelectedAttributeUI_folder():
    # import 
    global C

    # remove ui on closure of shelf
    for i in C :

        # avoid un-removable attributes
        try:
            attributesText_F[i] = cmds.deleteUI(i + "_aFF")
        except:
            continue

    # clear global array
    C = []


def updateSelectedAttributesLayer():
    #import
    global L
    # get shared attributes between selected objects
    for I in cmds.ls(sl=True) :
        A = cmds.listAttr(I, write=True)
        if L == [] :
            L = A
        else :
            L = set(L).intersection(A)
    # sort for ease of traversal
    L = sorted(L)
    updateSelectedAttributeUI_Layer()



def updateSelectedAttributeUI_Layer():
    global L
    for i in L :
        # remove attributes that "don't exist" but still apear (???)
        if "." not in i :
            attributesText_L[i] = cmds.textFieldGrp(i + "_aFL",label=i, parent="attributeColumn_L")

def clearSelectedAttributeUI_layer():
    # import 
    global L

    # remove ui on closure of shelf
    for i in L :

        # avoid un-removable attributes
        try:
            attributesText_L[i] = cmds.deleteUI(i + "_aFL")
        except:
            continue

    # clear global array
    L = []

# ------BUTTON CONNECTION------

def createFolder(*args):
    # attribute fetch
    folderName = cmds.textFieldGrp("ffGV", q=1, text=1)
    regex = cmds.textFieldGrp("rffGV", q=1, text=1)
    condition = cmds.textFieldGrp("cffGV", q=1, text=1)

    # allow for empty conditions
    if(condition == ""):
        condition = "True"
    
    # gain attribute conditions
    for y in C : 
        # avoid odd attributes that fail to read in exec() contect (??)
        try:
            # fetch
            attr = cmds.textFieldGrp(y + "_aFF", q=1, text=1)
            if attr != "" : 
                # append to condition for exec()
                condition += " and cmds.getAttr(X + '." + y + "') == " + attr
        except:
            continue

    # check for reorder
    if(cmds.checkBox("rC", q=1, v=True)):
            # check condition / use of each box / combination of boxes
            if condition != "True" and regex != "" :
                massRename.findConditionFolderOpen(condition, regex, folderName)
            if condition != "True" : 
                massRename.conditionalFolderOpen(condition, folderName)
            elif regex != "":
                massRename.findOpen(regex, folderName)
            else:
                massRename.createFolderOpen(folderName)
    else: 
            if condition != "True" and regex != "" :
                massRename.findConditionFolder(condition,regex,folderName)
            elif condition != "True" : 
                massRename.conditionalFolder(condition, folderName)
            elif regex != "":
                massRename.find(regex, folderName)
            else:
                massRename.createFolder(folderName)


def createLayer(*args):
    layerName = cmds.textFieldGrp("lfGV", q=1, text=1)
    regex = cmds.textFieldGrp("rlfGV", q=1, text=1)
    condition = cmds.textFieldGrp("clfGV", q=1, text=1)


    # allow for empty conditions
    if(condition == ""):
        condition = "True"
    
    # gain attribute conditions
    for y in L : 
        # avoid odd attributes that fail to read in exec() contect (??)
        try:
            # fetch
            attr = cmds.textFieldGrp(y + "_aFL", q=1, text=1)
            if attr != "" : 
                # append to condition for exec()
                condition += " and cmds.getAttr(X + '." + y + "') == " + attr
        except:
            continue

    if regex != "" and condition != "True" :
        massRename.shiftLayerSearchAndCondition(condition, regex, layerName)
    elif regex != "" :
        massRename.shiftLayerSearch(regex, layerName)
    elif condition !="True":
        massRename.shiftLayerCondition(condition, layerName)
    else:
        massRename.shiftLayer(layerName)

def cascadeAttributes(*args):
    folderName = cmds.textFieldGrp("efGV", q=1, text=1)
    code = cmds.textFieldGrp("cofGV", q=1, text=1)
    procedureCascade.cascadeFunctions(folderName, code)

def repeatLast(*args):
    folderName = cmds.textFieldGrp("efGV", q=1, text=1)
    procedureCascade.repeatLast(folderName)

def openDoc(*args):
    wb.open("https://ncca.github.io/pipeline-project-Geekwithahat/")




# ------ CREATION OF UI ------

# base creation
cmds.columnLayout("columnLayout", adjustableColumn=True, rowSpacing=10)
cmds.scrollLayout("SL", horizontalScrollBarThickness=16, verticalScrollBarThickness=16, height=600)

# folder management 
cmds.frameLayout("FFL", label="Folder Management", collapsable=True, collapse=False, parent="SL", marginWidth=10, marginHeight=10,
annotation="Folder Management: Creates folder objects from current items in the scene.")

folderFieldGrpVar = cmds.textFieldGrp("ffGV", label='Folder Name', text="", parent="FFL",
annotation="Folder Name: Provide a name for a folder object.")

regexF_FieldGrpVar = cmds.textFieldGrp("rffGV", label="Search", text="", parent="FFL",
annotation="Folder Search: Search for items by name and add them to a folder.")

conditionFieldGrpVar = cmds.textFieldGrp("cffGV", label='Condition',
annotation="Condition Folder: Search for items by attribute \n Current item reffered to as X.", text="",parent="FFL")


# attribute frame
cmds.frameLayout(label=f"Shared attributes (Advanced Search)", collapsable=True, collapse=True, 
preExpandCommand=updateSelectedAttributesFolder, preCollapseCommand=clearSelectedAttributeUI_folder,
parent="FFL", marginWidth=10, marginHeight=10,
annotation="Display all attributes common between current selection.")

# allow for buttons
cmds.columnLayout("attributeColumn_F", adjustableColumn=True)

# assign attribute ui to frame
cmds.setParent("..")
cmds.setParent("..")




reorgCheck = cmds.checkBox("rC", label="Reorder", align="centre",
annotation="Reogranisation: Removed objects from folders before placing them in a new folder.")

cmds.button( label='Create Folder', command=createFolder,
annotation="Create Folder: Sources from selection or from above parameters." )


# layer management
cmds.frameLayout("LFL", label="Layer Management", collapsable=True, collapse=False, parent="SL", marginWidth=10, marginHeight=10,
annotation="Layer Management: Creates a display layer from current items in the scene.")

layerFieldGrpVar = cmds.textFieldGrp("lfGV", label='Layer Name', text="", parent="LFL",
annotation="Layer Name: Provide a name for display layer." )

regexL_FieldGrpVar = cmds.textFieldGrp("rlfGV", label='Search', text="", parent="LFL",
annotation="Layer Search: Search for items by item name and add them to a display layer." )

conditionFieldGrpVar = cmds.textFieldGrp("clfGV", label='Condition',
annotation="Condition Layer: Search for items by attribute \n Current item reffered to as X.", text="", parent="LFL")


# attribute frame
cmds.frameLayout(label=f"Shared attributes (Advanced Search)", collapsable=True, collapse=True, 
preExpandCommand=updateSelectedAttributesLayer, preCollapseCommand=clearSelectedAttributeUI_layer,
parent="LFL", marginWidth=10, marginHeight=10, annotation="Display all attributes comon between current selection.")

# allow for buttons
cmds.columnLayout("attributeColumn_L", adjustableColumn=True)

# assign attribute ui to frame
cmds.setParent("..")
cmds.setParent("..")


cmds.button( label='Create Layer', command=createLayer,
annotation="Create Layer: Sources from selection or from above parameters." )


# function cascade
cmds.frameLayout("CFL", label="Cascade Management", collapsable=True, collapse=False, parent="SL", marginWidth=10, marginHeight=10,
annotation="Cascade Management: Performs a given function on each item in a given folder." )

ElementsFieldGrpVar = cmds.textFieldGrp("efGV", label='Folder Name', text="", parent="CFL",
annotation="Folder Name: Provide the existing folder to cascade a procedure through." )

code_FieldGrpVar = cmds.textFieldGrp("cofGV", label='Code', text="", parent="CFL",
annotation="Cascade Function: Python function to be applied to each object in a folder." )

cmds.button( label='Execute', command=cascadeAttributes, parent="CFL",
annotation="Execute: Apply function to each object in a folder.")

cmds.button( label='Repeat Last', command=repeatLast, parent="CFL",
annotation="Cascade Function: Python function to be applied to each objects in a folder.")

# Documentation open
cmds.button(label="Help", command=openDoc, parent="SL",
annotation="Help: Open documentation in a browser.")

# allow for docking
cmds.dockControl("bigUI", label="Big Manager", area='left', content="columnLayout", allowedArea="all")

