import maya.cmds as cmds
import massRename
import procedureCascade



folderName = "none"

attributesText = {}
attributesCondition = {}
C = []


def updateSelectedAttributes(*args):
    global C
    for I in cmds.ls(sl=True) :
        cmds.select(I)
        A = cmds.listAttr(I, write=True)
        print(I)
        if C == [] :
            C = A
        else :
            for x in C :
                for y in A :
                    if x == y :
                        C += [x]


def createFolder(*args):
    if(cmds.checkBox(reorgCheck, q=1, v=True)):
        folderName = cmds.textFieldGrp(folderFieldGrpVar, q=1, text=1)
        regex = cmds.textFieldGrp(regexF_FieldGrpVar, q=1, text=1)
        condition = cmds.textFieldGrp(conditionFieldGrpVar, q=1, text=1)
        if condition != "" : 
            massRename.conditionalFolderOpen(condition, folderName)
        else:
            massRename.findOpen(regex, folderName)
    else: 
        folderName = cmds.textFieldGrp(folderFieldGrpVar, q=1, text=1)
        regex = cmds.textFieldGrp(regexF_FieldGrpVar, q=1, text=1)
        condition = cmds.textFieldGrp(conditionFieldGrpVar, q=1, text=1)
        if condition != "" : 
            massRename.conditionalFolder(condition, folderName)
        else:
            massRename.find(regex, folderName)
    
    updateSelectedAttributes()

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




UPPER_WINDOW = cmds.window("Big Manager")

MAIN_WINDOW = cmds.columnLayout(adjustableColumn=True, parent=UPPER_WINDOW )

cmds.text(label="Folder Management     ", align='right', font='boldLabelFont', parent=MAIN_WINDOW)
cmds.text( label='Folder Name', parent=MAIN_WINDOW )
folderFieldGrpVar = cmds.textFieldGrp(parent=MAIN_WINDOW)
cmds.text(label='Search', parent=MAIN_WINDOW)
regexF_FieldGrpVar = cmds.textFieldGrp(parent=MAIN_WINDOW)
cmds.text(label='Condition', annotation="Current item refered to as X.", parent=MAIN_WINDOW)
conditionFieldGrpVar = cmds.textFieldGrp( parent=MAIN_WINDOW)



cmds.frameLayout(label=f"Shared attributes ({len(C)})", collapsable=True, collapse=False, parent=MAIN_WINDOW)
cmds.columnLayout(adjustableColumn=True, parent=MAIN_WINDOW)



for i in C :
    cmds.text(label=i)
    attributesText[i] = cmds.textFieldGrp(cc=Test(i))
cmds.setParent('..')
cmds.setParent('..')




reorgCheck = cmds.checkBox(label="Reorder", parent=MAIN_WINDOW)
cmds.button( label='Create Folder', command=createFolder, parent=MAIN_WINDOW )

cmds.text(label="Layer Management    ", align='right', font='boldLabelFont', parent=MAIN_WINDOW)
cmds.text( label='Layer Name', parent=MAIN_WINDOW )
layerFieldGrpVar = cmds.textFieldGrp( parent=MAIN_WINDOW)
cmds.text(label='Search', parent=MAIN_WINDOW)
regexL_FieldGrpVar = cmds.textFieldGrp( parent=MAIN_WINDOW)
cmds.button( label='Create Layer', command=createLayer, parent=MAIN_WINDOW )

cmds.text(label="Function Cascade    ", align='right', font='boldLabelFont', parent=MAIN_WINDOW)
cmds.text( label='Folder Name', parent=MAIN_WINDOW)
ElementsFieldGrpVar = cmds.textFieldGrp( parent=MAIN_WINDOW)
cmds.text(label='Code', parent=MAIN_WINDOW)
code_FieldGrpVar = cmds.textFieldGrp( parent=MAIN_WINDOW)
cmds.button( label='Execute', command=cascadeAttributes, parent=MAIN_WINDOW )
cmds.button( label='Repeat Last', command=repeatLast, parent=MAIN_WINDOW)

cmds.dockControl(label="Big Manager", area='left', content=UPPER_WINDOW, parent=MAIN_WINDOW )

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