import maya.api.OpenMaya as om
import maya.cmds as cmds
import importlib.util
import sys
import os

maya_useNewAPI = True


class BigMaya(om.MPxCommand):
    CMD_NAME = "BigInit"

    def __init__(self):
        super(BigMaya, self).__init__()

    def doIt(self, args):
        """
        Called when the command is executed in script
        """
        print("Loading Big Manager.....")


        # Get the directory of the current file
        path = cmds.moduleInfo(path=True, moduleName="bigManager")
        path += "/scripts/big_ui.py"

        # Load the module
        spec = importlib.util.spec_from_file_location("big_ui", path)
        data = importlib.util.module_from_spec(spec)
        sys.modules["big_ui"] = data
        spec.loader.exec_module(data)

    @classmethod
    def creator(cls):
        """
        Think of this as a factory
        """
        return BigMaya()

    
    

    


def initializePlugin(plugin):
    """
    Load our plugin
    """
    vendor = "WIFI_NULL"
    version = "1.0.0"

    plugin_fn = om.MFnPlugin(plugin, vendor, version)

    try:
        plugin_fn.registerCommand(BigMaya.CMD_NAME, BigMaya.creator)
    except:
        om.MGlobal.displayError(
            "ERROR ERROR : Failed to register command: {0}".format(BigMaya.CMD_NAME)
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

    plugin_name = "bigInit.py"

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
