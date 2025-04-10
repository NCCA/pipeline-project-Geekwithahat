import pytest

import sys, os
import maya.standalone


def setup_module(module):
    maya.standalone.initialize(name="python")
    import maya.cmds as cmds

    # add the current directory to the MAYA_PLUG_IN_PATH
    print("initializing maya-standalone")


def teardown_module(module):
    print("closing down maya-standalone")
    maya.standalone.uninitialize()

def test_givenFunction():

    import maya.cmds as cmds

    cmds.sphere(n="test")
    cmds.select("test")
    y = len(cmds.ls(selection=True))

    assert y == 1

