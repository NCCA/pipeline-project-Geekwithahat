import maya.cmds as cmds
import massRename
import procedureCascade



folderName = "none"

def createFolder(*args):
    if(cmds.checkBox(reorgCheck, q=1, v=True)):
        folderName = cmds.textFieldGrp(folderFieldGrpVar, q=1, text=1)
        regex = cmds.textFieldGrp(regexF_FieldGrpVar, q=1, text=1)
        massRename.findOpen(regex, folderName)
    else: 
        folderName = cmds.textFieldGrp(folderFieldGrpVar, q=1, text=1)
        regex = cmds.textFieldGrp(regexF_FieldGrpVar, q=1, text=1)
        massRename.find(regex, folderName)

def createFolderCondition(*args):
    if(cmds.checkBox(reorgCheck, q=1, v=True)):
        folderName = cmds.textFieldGrp(folderFieldGrpVar, q=1, text=1)
        condition = cmds.textFieldGrp(conditionFieldGrpVar, q=1, text=1)
        massRename.conditionalFolderOpen(condition, folderName)
    else:
        folderName = cmds.textFieldGrp(folderFieldGrpVar, q=1, text=1)
        condition = cmds.textFieldGrp(conditionFieldGrpVar, q=1, text=1)
        massRename.conditionalFolder(condition, folderName)

def createLayer(*args):
    layerName = cmds.textFieldGrp(layerFieldGrpVar, q=1, text=1)
    regex = cmds.textFieldGrp(regexL_FieldGrpVar, q=1, text=1)
    massRename.shiftLayer(regex, layerName)

def cascadeAttributes(*args):
    folderName = cmds.textFieldGrp(ElementsFieldGrpVar, q=1, text=1)
    code = cmds.textFieldGrp(code_FieldGrpVar, q=1, text=1)
    procedureCascade.cascadeFunctions(folderName, code)

def repeatLast(*args):
    folderName = cmds.textFieldGrp(ElementsFieldGrpVar, q=1, text=1)
    procedureCascade.repeatLast(folderName)

def reRun(*args):
    cmds.window("Big Manager")
    cmds.columnLayout()

    cmds.text( label='Folder Name' )
    folderFieldGrpVar = cmds.textFieldGrp()
    cmds.text(label='Search')
    regexF_FieldGrpVar = cmds.textFieldGrp()
    cmds.text(label='Condition')
    conditionFieldGrpVar = cmds.textFieldGrp()
    reorgCheck = cmds.checkBox(label="Reorder")
    cmds.button( label='Create Folder', command=createFolder )

    cmds.text( label='Layer Name' )
    layerFieldGrpVar = cmds.textFieldGrp()
    cmds.text(label='Search')
    regexL_FieldGrpVar = cmds.textFieldGrp()
    cmds.button( label='Create Layer', command=createLayer )

    cmds.text( label='Folder Name' )
    ElementsFieldGrpVar = cmds.textFieldGrp()
    cmds.text(label='Code')
    code_FieldGrpVar = cmds.textFieldGrp()
    cmds.button( label='Execute', command=cascadeAttributes )
    cmds.showWindow()





cmds.window("Big Manager")
cmds.columnLayout(adjustableColumn=True )

cmds.text(label="Folder Management", align='right', font='boldLabelFont')
cmds.text( label='Folder Name' )
folderFieldGrpVar = cmds.textFieldGrp()
cmds.text(label='Search')
regexF_FieldGrpVar = cmds.textFieldGrp()
cmds.text(label='Condition')
conditionFieldGrpVar = cmds.textFieldGrp()
cmds.frameLayout(label="Section 1", collapsable=True, collapse=False, borderStyle='etchedOut')
reorgCheck = cmds.checkBox(label="Reorder")
cmds.button( label='Create Folder', command=createFolder )

cmds.text(label="Layer Management", align='right', font='boldLabelFont')
cmds.text( label='Layer Name' )
layerFieldGrpVar = cmds.textFieldGrp()
cmds.text(label='Search')
regexL_FieldGrpVar = cmds.textFieldGrp()
cmds.button( label='Create Layer', command=createLayer )

cmds.text(label="Function Cascade", align='right', font='boldLabelFont')
cmds.text( label='Folder Name' )
ElementsFieldGrpVar = cmds.textFieldGrp()
cmds.text(label='Code')
code_FieldGrpVar = cmds.textFieldGrp()
cmds.button( label='Execute', command=cascadeAttributes )
cmds.button( label='Repeat Last', command=repeatLast)


cmds.showWindow()



# def Test(*args) :
#     attributesCondition[attributesText[args]] = cmds.textFieldGrp(attributesText[args], q=1, text=1)

# cmds.window("Big Manager")
# cmds.columnLayout(adjustableColumn=True )
# cmds.frameLayout(label="Section 2", collapsable=True, collapse=True, borderStyle='etchedOut')

# attributesText = {}
# attributesCondition = {}

# C = []


# for I in cmds.ls(sl=True) :
#     cmds.select(I)
#     A = cmds.listAttr(I, write=True)
#     print(I)
#     if C == [] :
#         C = A
#     else :
#         for x in C :
#             for y in A :
#                 if x == y :
#                     C += [x]

# for i in C :
#     cmds.text(label=i)
#     attributesText[i] = cmds.textFieldGrp(cc=Test(i))

# cmds.showWindow()