import maya.cmds as cmds
import massRename
import procedureCascade



folderName = "none"

def createFolder(*args):
    folderName = cmds.textFieldGrp(folderFieldGrpVar, q=1, text=1)
    regex = cmds.textFieldGrp(regexF_FieldGrpVar, q=1, text=1)
    massRename.find(regex, folderName)

def createLayer(*args):
    layerName = cmds.textFieldGrp(layerFieldGrpVar, q=1, text=1)
    regex = cmds.textFieldGrp(regexL_FieldGrpVar, q=1, text=1)
    massRename.shiftLayer(regex, layerName)

def cascadeAttributes(*args):
    folderName = cmds.textFieldGrp(ElementsFieldGrpVar, q=1, text=1)
    code = cmds.textFieldGrp(code_FieldGrpVar, q=1, text=1)
    procedureCascade.cascadeFunctions(folderName, code)

cmds.window("Big Manager")
cmds.columnLayout()

cmds.text( label='Folder Name' )
folderFieldGrpVar = cmds.textFieldGrp()
cmds.text(label='Search')
regexF_FieldGrpVar = cmds.textFieldGrp()
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


