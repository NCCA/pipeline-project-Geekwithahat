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
    if(cmds.checkBox("rC", q=1, v=True)):
        folderName = cmds.textFieldGrp("ffGV", q=1, text=1)
        regex = cmds.textFieldGrp("rffGV", q=1, text=1)
        condition = cmds.textFieldGrp("cfGV", q=1, text=1)
        if condition != "" : 
            massRename.conditionalFolderOpen(condition, folderName)
        else:
            massRename.findOpen(regex, folderName)
    else: 
        folderName = cmds.textFieldGrp("ffGV", q=1, text=1)
        regex = cmds.textFieldGrp("rffGV", q=1, text=1)
        condition = cmds.textFieldGrp("cfGV", q=1, text=1)
        if condition != "" : 
            massRename.conditionalFolder(condition, folderName)
        else:
            massRename.find(regex, folderName)
    
    updateSelectedAttributes()

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




MAIN_WINDOW = cmds.columnLayout(adjustableColumn=True)
cmds.text(label="Folder Management     ", align='right', font='boldLabelFont')
folderFieldGrpVar = cmds.textFieldGrp("ffGV", label='Folder Name', text="")
regexF_FieldGrpVar = cmds.textFieldGrp("rffGV", label="Search", text="")
conditionFieldGrpVar = cmds.textFieldGrp("cfGV", label='Condition', annotation="Current item refered to as X.", text="")



cmds.frameLayout(label=f"Shared attributes ({len(C)})", collapsable=True, collapse=False)
cmds.columnLayout(adjustableColumn=True)



for i in C :
    cmds.text(label=i)
    attributesText[i] = cmds.textFieldGrp(cc=Test(i))
cmds.setParent('..')
cmds.setParent('..')




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


allowedAreas = ['right', 'left']
cmds.dockControl( label="Big Manager", area='left', content=MAIN_WINDOW, allowedArea=allowedAreas )


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