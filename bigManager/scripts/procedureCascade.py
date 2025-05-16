'''
Allow for repeated functions on every 
'''

#------ IMPORTS ------

import maya.cmds as cmds
import os
import re
import maya.mel as mel 


# ------ FUNCTION CASCADE ------

def cascadeFunctions(Folder, Code) :
    try:
        # every object
        cmds.select(clear=True)
        Reg = "^"+Folder+"_.*"
        for i in cmds.ls(typ="transform") :
            if(re.findall(Reg, i) != []):
                cmds.select(i, add=True)
        x = cmds.ls(sl=True, typ="transform")

        # apply function to each
        for o in x :
            cmds.select(o)
            exec(Code)
    except:
        cmds.warning("Provided code error.")



# ------ REPEAT PREVIOUS COMMAND ------

def repeatLast(Folder) :
    try:
        if(cmds.getAttr(Folder + ".FolderFlag")) : 
            # every object
            cmds.select(clear=True)
            Reg = "^"+Folder+"_.*"
            for i in cmds.ls(typ="transform") :
                if(re.findall(Reg, i) != []):
                    cmds.select(i, add=True)
            x = cmds.ls(sl=True, typ="transform")

            # apply previous function for each object in folder
            for o in x :
                cmds.select(o)
                mel.eval("RepeatLast")
        else:
            cmds.warning("Please provide an appropriate folder.") 
    except:
        cmds.warning("Please provide an appropriate folder.")      
    
