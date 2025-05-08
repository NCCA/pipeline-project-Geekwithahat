import maya.cmds as cmds
import massRename
import procedureCascade



folderName = "none"

attributesText = {}
attributesCondition = {}
C = []


if cmds.dockControl("bigUI",exists=True) :
    cmds.deleteUI("bigUI")




def updateSelectedAttributes():
    global C
    for I in cmds.ls(sl=True) :
        A = cmds.listAttr(I, write=True)
        if C == [] :
            C = A
        else :
            C = set(C).intersection(A)
    updateSelectedAttributeUI()



def updateSelectedAttributeUI():
    global C
    for i in C :
        attributesText[i] = cmds.textFieldGrp(i + "_aFF",label=i, parent="attributeColumn")

def clearSelectedAttributeUI():
    global C
    for i in C :
        try:
            attributesText[i] = cmds.deleteUI(i + "_aFF")
        except:
            continue
    C = []


def createFolder(*args):
    folderName = cmds.textFieldGrp("ffGV", q=1, text=1)
    regex = cmds.textFieldGrp("rffGV", q=1, text=1)
    condition = cmds.textFieldGrp("cfGV", q=1, text=1)

    if(condition == ""):
        condition = "True"
    
    for y in C : 
        try:
            attr = cmds.textFieldGrp(y + "_aFF", q=1, text=1)
            print(attr)
            if attr != "" : 
                condition += " and cmds.getAttr(X + '." + y + "') == " + attr
        except:
            continue


    if(cmds.checkBox("rC", q=1, v=True)):
        if condition != "" : 
            massRename.conditionalFolderOpen(condition, folderName)
        else:
            massRename.findOpen(regex, folderName)
    else: 
        if condition != "" : 
            massRename.conditionalFolder(condition, folderName)
        else:
            massRename.find(regex, folderName)

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


cmds.columnLayout("columnLayout", adjustableColumn=True)
cmds.scrollLayout( horizontalScrollBarThickness=16, verticalScrollBarThickness=16)
cmds.text(label="Folder Management     ", align='right', font='boldLabelFont')
folderFieldGrpVar = cmds.textFieldGrp("ffGV", label='Folder Name', text="")
regexF_FieldGrpVar = cmds.textFieldGrp("rffGV", label="Search", text="")
conditionFieldGrpVar = cmds.textFieldGrp("cfGV", label='Condition', annotation="Current item refered to as X.", text="")



cmds.frameLayout(label=f"Shared attributes", collapsable=True, collapse=True, 
preExpandCommand=updateSelectedAttributes, preCollapseCommand=clearSelectedAttributeUI)

cmds.columnLayout("attributeColumn", adjustableColumn=True)

cmds.setParent("..")
cmds.setParent("..")




reorgCheck = cmds.checkBox("rC", label="Reorder")
cmds.button( label='Create Folder', command=createFolder )

cmds.text(label="Layer Management    ", align='right', font='boldLabelFont')
layerFieldGrpVar = cmds.textFieldGrp("lfGV", label='Layer Name', text="")
regexL_FieldGrpVar = cmds.textFieldGrp("rlfGV", label='Search', text="")
cmds.button( label='Create Layer', command=createLayer )

cmds.text(label="Function Cascade    ", align='right', font='boldLabelFont')
ElementsFieldGrpVar = cmds.textFieldGrp("efGV", label='Folder Name', text="")
code_FieldGrpVar = cmds.textFieldGrp("cofGV", label='Code', text="")
cmds.button( label='Execute', command=cascadeAttributes)
cmds.button( label='Repeat Last', command=repeatLast)


cmds.dockControl("bigUI", label="Big Manager", area='left', content="columnLayout")