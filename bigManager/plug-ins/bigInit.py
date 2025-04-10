# import * from massRename

# def main():
#     print("Hello from bigmanager!")

# def initializePlugin(self):
#     print("Initializing..... kindly stop complaining....")

# def uninitializePlugin(self):
#     print("Turning off..... kindly stop complaining.....")



# if __name__ == "__main__":
#     main()

# def debug() -> int:
#     print("debugging big init")
#     return 1

import maya.api.OpenMaya as om
import maya.cmds as cmds
import re

'''
def maya_useNewAPI():
    """
    Can either use this function (which works on earlier versions)
    or we can set maya_useNewAPI = True
    """
    pass
'''

maya_useNewAPI = True


class BigMaya(om.MPxCommand):
    CMD_NAME = "BigMaya"

    def massRename(name) -> None :
        cmds.select(name, hierarchy = True)
        selected = cmds.ls(selection=True)
        
        assetName = selected[0]
        
        replace = {}
        
        for c in selected :
            cN = re.findall("[A-Z, a-z 0-9, ^|_]*[a-z, A-Z]", c)[0]
            if (cN == assetName) | ("|" in cN) | (re.search(".*Shape", cN) != None) | (c in replace):
                continue
            replace[c] = assetName + "_" + cN
        
        
        for rn in selected : 
            if (rn == assetName) | ('|' in rn) | ("Shape" in rn) | (assetName in rn):
                continue
            print(rn)
            cmds.select(rn)
            cmds.rename(replace[rn])
        
    def defaultButtonPush(*args):
        print ('Button 1 was pushed.')



    def createFolder(folderName) -> None :
        cmds.group(n=folderName)
        massRename(folderName)

    def find(regEx, folderName) -> None :
        x = cmds.ls(geometry=True) 
        cmds.group(x, n="TEST")
        createFolder(folderName) 

    def __init__(self):
        super(BigMaya, self).__init__()

    def doIt(self, args):
        """
        Called when the command is executed in script
        """
        print("HELLO FROM BIG INIT")
        om.MGlobal.displayWarning("BIG WARNING")
        om.MGlobal.displayError("BIG ERROR")
        om.MGlobal.displayInfo("BIG INFO")

        cmds.window( width=150 )
        cmds.columnLayout( adjustableColumn=True )
        cmds.button( label='Button 1', command=defaultButtonPush )
        cmds.showWindow()

    @classmethod
    def creator(cls):
        """
        Think of this as a factory
        """
        return BigMaya()

class TestButton(om.MPxCommand) :
    CMD_NAME = "TestButton"

    def __init__(self):
        super(TestButton, self).__init__()

    def doIt(self, args) :
        print("do it test")
    
    @classmethod
    def creator(cls):
        return TestButton()
    
    

    


def initializePlugin(plugin):
    """
    Load our plugin
    """
    vendor = "WIFI_NULL"
    version = "0.1.0"

    plugin_fn = om.MFnPlugin(plugin, vendor, version)

    try:
        plugin_fn.registerCommand(BigMaya.CMD_NAME, BigMaya.creator)
    except:
        om.MGlobal.displayError(
            "Failed to register command: {0}".format(BigMaya.CMD_NAME)
        )


def uninitializePlugin(plugin):
    """
    Exit point for a plugin
    """
    plugin_fn = om.MFnPlugin(plugin)
    try:
        plugin_fn.deregisterCommand(BigMaya.CMD_NAME)
    except:
        om.MGlobal.displayError(
            "Failed to deregister command: {0}".format(BigMaya.CMD_NAME)
        )


if __name__ == "__main__":
    """
    So if we execute this in the script editor it will be a __main__ so we can put testing code etc here
    Loading the plugin will not run this
    As we are loading the plugin it needs to be in the plugin path.
    """

    plugin_name = "BigMaya.py"

    cmds.evalDeferred(
        'if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(
            plugin_name
        )
    )
    cmds.evalDeferred(
        'if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(
            plugin_name
        )
    )
