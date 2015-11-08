#!/usr/bin/env python3
import sys, os, re, string

# Check if the module name was given as command line argument
if len(sys.argv) != 2:
    print("Usage: lms-create-lib <library_name>")
    sys.exit(1)

# Library's name (e.g. test_lib)
library_name = sys.argv[1]

if(library_name == ""):
    print("Library name must not be empty")
    sys.exit(1)

if("/" in library_name or "\\" in library_name):
    print("Library name must not contain / or \\")
    sys.exit(1)

try:
    os.mkdir(library_name)
    os.mkdir(os.path.join(library_name, "src"))
    os.mkdir(os.path.join(library_name, "include"))
    os.mkdir(os.path.join(library_name, "include", library_name))
except FileExistsError:
    print("Library directory is already existing: {0}".format(module_name))
    sys.exit(1)

params = {
    "library" : library_name,
}

def write_templ_file(file, content):
    with open(os.path.join(library_name, *file), "w") as f:
        f.write(string.Template(content).substitute(**params))

write_templ_file(["CMakeLists.txt"],
"""set(SOURCES
# src/file.cpp
)

set(HEADERS
# include/${library}/file.h
)

include_directories(include)
add_library(${library} SHARED $${SOURCES} $${HEADERS})
target_link_libraries(${library} PRIVATE lmscore)
""")

write_templ_file(["README.md"],
"""# ${library}

## Dependencies
""")

# Create empty file
write_templ_file(["include", "CMakeSharedHeaders.txt"], "")
