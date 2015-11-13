#!/usr/bin/env python3
import sys
from lms import generator

# Check if the module name was given as command line argument
if len(sys.argv) != 2:
    print("Usage: lms-create-mod <module_name>")
    sys.exit(1)

# Module's name (e.g. module_name)
module_name = sys.argv[1]

if(module_name == ""):
    print("Module name must not be empty")
    sys.exit(1)

if("/" in module_name or "\\" in module_name):
    print("Module name must not contain / or \\")
    sys.exit(1)

try:
    generator.mktree(".", {
        module_name : {
            "CMakeLists.txt" : generator.MOD_CMAKE,
            "README.md" : generator.MOD_README,
            "src" : {
                module_name + ".cpp" : generator.MOD_SOURCE,
                "interface.cpp" : generator.MOD_INTERFACE
            },
            "include" : {
                module_name + ".h" : generator.MOD_HEADER
            }
        }
    }, {
        "module" : module_name,
        # Generate an uppercase version for header include guards (e.g. TEST_MODULE)
        "module_upper" : module_name.upper(),
        # Generate a camelcase version for the class name (e.g. TestModule)
        "module_camel" : generator.camel_case(module_name)
    })

except FileExistsError:
    print("Module creation failed")
    sys.exit(1)
