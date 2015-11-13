#!/usr/bin/env python3
import sys
from lms import generator

# Check if the library name was given as command line argument
if len(sys.argv) != 2:
    print("Usage: lms-create-lib <library_name>")
    sys.exit(1)

# Library's name (e.g. test_lib)
library_name = sys.argv[1]

if library_name == "" :
    print("Library name must not be empty")
    sys.exit(1)

if "/" in library_name or "\\" in library_name:
    print("Library name must not contain / or \\")
    sys.exit(1)

try:
    generator.mktree(".", {
        library_name : {
            "CMakeLists.txt" : generator.LIB_CMAKE,
            "README.md" : generator.LIB_README,
            "src" : {},
            "include" : {
                "CMakeSharedHeaders.txt" : "",
                library_name : {}
            }
        }
    }, {
        "library" : library_name
    })
except FileExistsError:
    print("Library creation failed")
    sys.exit(1)
