[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Tn7g_Mhz)

# Big - Maya Large Scene Procedure Tool

Creating a tool within Maya for reformatting large scenes that have become difficult to manage without computational solutions, including renaming, grouping and mass-applying tools and procedures. Works with both the pre-existing editor, extends it to allow for quick access to certain functions, and can allow for the use of shelf tools. Focusing more on a scene with several objects that may need to be altered similarly.

# Use

Run installModFile.py

Run cmds.BigInit() in Maya's Script editor

# Functionality

## __Folder Creation__

Creates a Folder group, renaming everything within the folder to prepend the folder name, removing the number from the object's name and restarting Maya's numbering system for that group.

**Selection Folder**

By default, objects selected within the scene are placed in a folder and reformatted.

**Search Folder**

By providing a RegEx value as a search variable, each object whose names matches the RegEx functions are placed in a folder and reformatted.

**Condition Folder**

By providing a Maya Python command, each item within a scene that evaluates the command True is placed in a given folder. 

*The currently evaluated item is stored in a given variable X.*

**Shared Attributes**

Presents a list of attributes common between the currently selected objects, presenting an input box for each attribute, allowing for a folder to be created with each value being equal between all members of the folder. 

**Re-Order**

A check-box allowing for attributes already within a folder to be removed from said group and placed into a different folder.

## __Layer Creation__ 

Places specified objects in a display layer of a given name, allowing for toggled visibility. 

**Selection Layer**

Places current selection into a display layer.

**Search Layer**

Places objects of a name matching a RegEx string into a display layer.

**Condition Folder**

Places objects passing an evaluated python condition into a display later.

*The currently evaluated item is stored in a given variable X.*

**Shared Attributes**

Presents a list of common attributes between the currently selected objects, presenting an input box for each attribute, allowing for a display layer to be created with each value being equal between all members of the layer.

## __Function Cascade__

When provided a folder and appropriate code, each item within the folder is selected and have the inputted procedure ran.

**Repeat Last**

Applies the last-ran action to each object within a provided folder name.

# Known issues and Errors

|**Known Issue**|**Error Level**|**Priority**
|---------|---------------|------------------|
|Fails to add particle system to folders|Function error|Low|
|Fails to load on boot instead of command run|Boot error|Low?|
|Unit test for repeat last action fails unreliably|Test error|Medium|

# Modules

## big_test
  
runAll() - runs all unit tests.

## big_ui

All functions are internal, boots the user interface for Big Manager on import. 

## Mass Rename

**massRename**
    
Mass Formats all new members of a folder by pre-pending name (For formatting folder name).

**createFolder**

Creates folder from selection.

**createFolderOpen**
  
Creates folder from selection, unparents objects from pre-existing folders.

**find**

Creates a folder from objects whose names match the regex function provided.

**findOpen**

Creates a folder from objects whose names match the regex function provided, unparents objects from pre-existing folders.

**conditionalFolder**

Creates a folder from objects that match the given python function. Mostly useful for Cmds.getAttr() functions. Each evaluated function is referered to as X.

**conditionalFolderOpen**

Creates a folder from objects that match the given python function, unparents objects from pre-existing folders. Mostly useful for Cmds.getAttr() functions. Each evaluated function is referered to as X.

**findConditionFolder**
Creates a folder from objects that both match the regex function and the given python function. Mostly useful for Cmds.getAttr() functions. Each evaluated function is referered to as X.

**findConditionFolderOpen**
    
Creates a folder from objects that both match the regex function and the given python function, unparents objects from pre-existing folders. Mostly useful for Cmds.getAttr() functions. Each evaluated function is referered to as X.

**cleanFolders**

Removes folder objects without items within them. Automatically called whenever an Open function is called.

## Procedure Cascade

**cascadeFunctions**

Runs a given function over each object in a folder

**repeatLast**

Repeats the last ran function on every item in a folder
