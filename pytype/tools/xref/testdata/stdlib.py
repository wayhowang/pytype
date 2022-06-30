# pylint: skip-file

from pytype.tools import path as path_tools
import os

#- @path ref vname(":module:", "pystdlib", _, "pytd:os.path", "python")
#- @split ref vname("module.split", "pystdlib", _, "pytd:os.path", "python")
path_tools.split("/x/y")
