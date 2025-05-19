import massRename
import procedureCascade
import maya.cmds as cmds

'''
Initial Testing for basic functionality within the Plugin without UI.

Methods
-------

runAll()
    Run all tests for Big Manager.

test_pytest()
    test testing

test_mayaTest()
    test maya.cmds

test_massRename()
    test massRename function

test_createFolder()
    test folder creation

test_regex()
    test creation from regex 

test_layerShift()
    test display creation

test_Cascade()
    test cascading function

test_RepeatLast()
    test repeat function for shelf
'''

def runAll():
    test_pytest()
    test_mayaTest()
    test_massRename()
    test_createFolder()
    test_regex()
    test_layerShift()
    test_Cascade()


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
    obj = cmds.ls("F","F_A","F_B", "F_C") 
    assert obj == ['F', 'F_A', 'F_B']
    cmds.delete("F")

    cmds.sphere(name = "A")
    cmds.sphere(name = "B")
    cmds.select("A","B")
    cmds.group(name = "A")
    massRename.massRename("A")
    obj = cmds.ls("A","A_A","A_B", "A_C") 
    assert obj == ['A', 'A_A', 'A_B']
    cmds.delete("A")

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
    obj = cmds.ls("F","F_A","F_A1", "F_A2")
    assert obj == ['F', 'F_A', 'F_A1', 'F_A2']
    cmds.delete("F")

def test_layerShift():
    print("--TESTING LAYER MOVEMENT--")
    cmds.sphere(name = "A1")
    cmds.sphere(name = "A2")
    cmds.sphere(name = "A3")
    massRename.shiftLayer("A","TEST")
    assert ['A1Shape', 'A1', 'A2', 'A2Shape', 'A3', 'A3Shape'] == cmds.editDisplayLayerMembers( "TEST", query=True )    
    cmds.delete("TEST")
    cmds.delete("A1", "A2", "A3")

def test_Cascade():
    print("--TESTING PREV FUNCTIONS")
    cmds.sphere(name = "A")
    cmds.sphere(name = "B")
    cmds.select("A","B")
    massRename.createFolder("F")
    procedureCascade.cascadeFunctions("F", "cmds.rename('test')")
    cmds.select("F", "test", "test1")
    obj = cmds.ls(sl=True)
    assert obj == ['F', 'test', 'test1']
    cmds.delete("F")

def test_RepeatLast():
    print("--TESTING REPEAT FUNCTION--")
    cmds.sphere(name = "A")
    cmds.select("A")
    massRename.createFolder("F")
    procedureCascade.repeatLast("F")
    cmds.select("F", "A","A1")
    obj = cmds.ls(sl=True)
    assert obj == ['F', 'A', 'A1']
    cmds.delete("F")






