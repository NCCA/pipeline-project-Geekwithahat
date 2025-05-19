import maya.api.OpenMaya as om
import maya.cmds as cmds
import importlib.util
import sys

maya_useNewAPI = True


class BigMaya(om.MPxCommand):
    CMD_NAME = "BigInit"

    def __init__(self):
        super(BigMaya, self).__init__()

    def doIt(self, args):
        '''
        Load and run big_ui on import.
        '''
        print("Loading Big Manager.....")


        # directory
        path = cmds.moduleInfo(path=True, moduleName="bigManager")
        path += "/scripts/big_ui.py"

        # Load module
        spec = importlib.util.spec_from_file_location("big_ui", path)
        data = importlib.util.module_from_spec(spec)
        sys.modules["big_ui"] = data
        spec.loader.exec_module(data)

    @classmethod
    def creator(cls):
        return BigMaya()

    
    

    


def initializePlugin(plugin):
    '''
    Info for Maya plugin window to display.
    '''
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

    plugin_name = "bigManager.py"

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
