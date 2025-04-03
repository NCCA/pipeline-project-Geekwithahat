[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Tn7g_Mhz)

__**Project Ideas:**__

- Maya Large Scene Procedure Tool

Creating a tool within Maya for reformatting large scenes that have become difficult to manage without computational solutions, including renaming, grouping and mass-applying tools and procedures. Works with both the pre-existing editor, extends it to allow for quick access to certain functions, and can allow for the use of shelf tools. Focusing more on a scene with several objects that may need to be altered similarly.

__**Possible functions**__

- Mass renaming (edit specifically long names to be unique, required due to previous export problems)

- Mass parenting (used for organisational purposes)

- Mass layer movement (^^^)

- Geometric function (i.e extrusion) on one object cascading to others

- Possible mass attribute editing and cascading attribute changes

- Possible organisational functions for complex scenes beyond this (i.e management ui)


__**Current Functionality**__

Basic bash scripts created in order to push and pull the current Maya Plugin back and forth from the location of the git repository and the current plugin path. 


__TO DO LIST:__

- Convert to an actual Maya module

- Mass renaming of long names
    - Take path, if given a name that is non-repeated, replace the last primitives with numbered versions of the found name.
