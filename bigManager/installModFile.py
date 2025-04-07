#!/usr/bin/env -S uv run --script

import argparse
import os
import platform
import sys
from pathlib import Path

maya_locations = {
    "Linux": "/maya/",
    "Darwin": "/Library/Preferences/Autodesk/maya",
    "Windows": "\\Documents\\maya\\",
}

MODULE_NAME = "bigManager"
VERSION = "0.1"
PYTHON_PATHS = "scripts"


def install_module(location, os):
    print(f"installing to {location}")
    # first write the module file
    current_dir = Path.cwd()
    # if the module folder doesn't exist make it
    module_dir = Path(location + "//modules")
    module_path = location + f"//modules/{MODULE_NAME}.mod"
    ## change to \\ for windows (easier then messing with Path objects)
    if os == "Windows":
        module_dir = Path(location + "\\modules")
        module_path = location + "modules\\{MODULE_NAME}.mod"
    module_dir.mkdir(exist_ok=True)

    if not Path(module_path).is_file():
        print("writing module file")
        with open(module_path, "w") as file:
            # Firs write out the module name and version with location
            file.write(f"+ {MODULE_NAME} {VERSION} {current_dir}\n")
            # we use += to append to the existing paths if it is
            # +:= Operator we appending with Higher Priority (pre-pend)
            file.write(f"MAYA_PLUG_IN_PATH += {current_dir}/plug-ins\n")
            file.write(f"scripts += {current_dir}/{PYTHON_PATHS}\n")
            file.write(f"PYTHONPATH += {current_dir}/{PYTHON_PATHS}\n")
            # Going to set some test ENVARS
            file.write(f"BIGMAN_PATH = {current_dir}\n")
    else : 
        print("ERROR MODULE FILE NOT FOUND")


def check_maya_installed(op_sys):
    mloc = f"{Path.home()}{maya_locations.get(op_sys)}"
    if not os.path.isdir(mloc):
        raise
    return mloc


if __name__ == "__main__":
    try:
        op_sys = platform.system()
        m_loc = check_maya_installed(op_sys)
    except:
        print("Error can't find maya install")
        sys.exit(-1)

    install_module(m_loc, op_sys)
