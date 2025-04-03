import re

cmds.select("comfy_chair", hierarchy = True)
selected = cmds.ls(selection=True)

assetName = selected[0]

print(assetName != selected[0])

print(selected)

for c in selected :
    if c != assetName :
        cN = re.
        cmds.select(c)
        newName = assetName + "_" + cN
        newName = re.sub("[0-9]*$","",newName)
        cmds.rename(assetName + "_" + cN)

# [A-Z, a-z 0-9]*[a-z, A-Z]
    
    
    