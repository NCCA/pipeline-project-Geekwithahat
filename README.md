[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Tn7g_Mhz)

# Big - Maya Large Scene Procedure Tool

Creating a tool within Maya for reformatting large scenes that have become difficult to manage without computational solutions, including renaming, grouping and mass-applying tools and procedures. Works with both the pre-existing editor, extends it to allow for quick access to certain functions, and can allow for the use of shelf tools. Focusing more on a scene with several objects that may need to be altered similarly.

# Functionality

## Folder Creation

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

|**Known Issue**|**Error Level**|
|---------|---------------|
|Folder name ends with a number|Crash / Catastrophic|
|Fails to add particle system to folders|Function error|
|Fails to remove empty folders|Function error|
|Internal Folder Inconcistency |Feature request|
|Renaming on re-order of folders|Feature request|


