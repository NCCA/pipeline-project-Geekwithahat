'''
UI creation in the basic Maya user interface library

todo: eventually convert to Qt?
'''

# ------IMPORTS------

import maya.cmds as cmds
import massRename
import procedureCascade


# ------GLOBAL VARIABLES------

folderName = "none"

attributesText = {}
attributesCondition = {}
C = []


# Remove existing UI if re-opened.
if cmds.dockControl("bigUI",exists=True) :
    cmds.deleteUI("bigUI")


# ------ATTRIBUTE IDENTIFICATION AND DISPLAY------


def updateSelectedAttributes():
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
    updateSelectedAttributeUI()



def updateSelectedAttributeUI():
    global C
    for i in C :
        # remove attributes that "don't exist" but still apear (???)
        if "." not in i :
            attributesText[i] = cmds.textFieldGrp(i + "_aFF",label=i, parent="attributeColumn")

def clearSelectedAttributeUI():
    # import 
    global C

    # remove ui on closure of shelf
    for i in C :

        # avoid un-removable attributes
        try:
            attributesText[i] = cmds.deleteUI(i + "_aFF")
        except:
            continue

    # clear global array
    C = []


# ------BUTTON CONNECTION------

def createFolder(*args):
    # attribute fetch
    folderName = cmds.textFieldGrp("ffGV", q=1, text=1)
    regex = cmds.textFieldGrp("rffGV", q=1, text=1)
    condition = cmds.textFieldGrp("cfGV", q=1, text=1)

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
    massRename.shiftLayer(regex, layerName)

def cascadeAttributes(*args):
    folderName = cmds.textFieldGrp("efGV", q=1, text=1)
    code = cmds.textFieldGrp("cofGV", q=1, text=1)
    procedureCascade.cascadeFunctions(folderName, code)

def repeatLast(*args):
    folderName = cmds.textFieldGrp("efGV", q=1, text=1)
    procedureCascade.repeatLast(folderName)



# ------ CREATION OF UI ------

# base creation
cmds.columnLayout("columnLayout", adjustableColumn=True)
cmds.scrollLayout( horizontalScrollBarThickness=16, verticalScrollBarThickness=16, height=600)

# folder management 
cmds.text(label="Folder Management     ", align='right', font='boldLabelFont')
folderFieldGrpVar = cmds.textFieldGrp("ffGV", label='Folder Name', text="")
regexF_FieldGrpVar = cmds.textFieldGrp("rffGV", label="Search", text="")
conditionFieldGrpVar = cmds.textFieldGrp("cfGV", label='Condition', annotation="Current item refered to as X.", text="")


# attribute frame
cmds.frameLayout(label=f"Shared attributes (Advanced Search)", collapsable=True, collapse=True, 
preExpandCommand=updateSelectedAttributes, preCollapseCommand=clearSelectedAttributeUI)

# allow for buttons
cmds.columnLayout("attributeColumn", adjustableColumn=True)

# assign attribute ui to frame
cmds.setParent("..")
cmds.setParent("..")




reorgCheck = cmds.checkBox("rC", label="Reorder")
cmds.button( label='Create Folder', command=createFolder )


# layer management
cmds.text(label="Layer Management    ", align='right', font='boldLabelFont')
layerFieldGrpVar = cmds.textFieldGrp("lfGV", label='Layer Name', text="")
regexL_FieldGrpVar = cmds.textFieldGrp("rlfGV", label='Search', text="")
cmds.button( label='Create Layer', command=createLayer )


# function cascade
cmds.text(label="Function Cascade    ", align='right', font='boldLabelFont')
ElementsFieldGrpVar = cmds.textFieldGrp("efGV", label='Folder Name', text="")
code_FieldGrpVar = cmds.textFieldGrp("cofGV", label='Code', text="")
cmds.button( label='Execute', command=cascadeAttributes)
cmds.button( label='Repeat Last', command=repeatLast)


# allow for docking
cmds.dockControl("bigUI", label="Big Manager", area='left', content="columnLayout")