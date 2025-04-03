import re

cmds.select("Spices", hierarchy = True)
selected = cmds.ls(selection=True)

assetName = selected[0]

replace = {}

for c in selected :
     cN = re.findall("[A-Z, a-z 0-9, ^|_]*[a-z, A-Z]", c)[0]
     if (cN == assetName) | ("|" in cN) | (re.search(".*Shape", cN) != None) | (c in replace):
         continue
     replace[c] = assetName + "_" + cN
# 

for rn in selected : 
    if (rn == assetName) | ('|' in rn) | ("Shape" in rn) | (assetName in rn):
        continue
    print(rn)
    cmds.select(rn)
    cmds.rename(replace[rn])

# get main name 

# get new name, skip if contains an existing name

# for each instance of old name replace with new name
