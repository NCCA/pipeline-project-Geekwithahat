#import pytest
import massRename
import maya.cmds as cmds
#import maya.standalone
#maya.standalone.initialize(name="python")

def runAll():
    test_pytest()
    test_mayaTest()
    test_massRename()
    test_createFolder()
    test_regex()


def test_pytest():
    print("--TESTING TESTING--")
    assert 1 == 1

def test_mayaTest():
    print("--TESTING MAYA--")
    cmds.sphere(name="test")
    x = cmds.ls("test")
    assert x[0] == "test"
    cmds.delete("test")

def test_massRename():
    print("--TESTING RENAME--")
    cmds.sphere(name = "A")
    cmds.sphere(name = "B")
    cmds.select("A","B")
    cmds.group(name = "F")
    massRename.massRename("F")
    O = cmds.ls("F","F_A","F_B", "F_C") 
    assert O == ['F', 'F_A', 'F_B']
    cmds.delete("F")

def test_createFolder():
    print("--TESTING FOLDER--")
    cmds.sphere(name = "A")
    cmds.sphere(name = "B")
    cmds.select("A","B")
    massRename.createFolder("F")
    O = cmds.ls("F","F_A","F_B", "F_C") 
    assert O == ['F', 'F_A', 'F_B']
    cmds.delete("F")

def test_regex():
    print("--TESTING REGEX--")
    cmds.sphere(name = "A1")
    cmds.sphere(name = "A2")
    cmds.sphere(name = "A3")
    massRename.find("A", "F")
    O = cmds.ls("F","F_A1","F_A2", "F_A3")
    assert O == ['F', 'F_A1', 'F_A2', 'F_A3']
    cmds.delete("F")






