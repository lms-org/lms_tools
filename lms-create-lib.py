#!/usr/bin/env python3
from lms import generator

generator.cli("lms-create-lib", lambda library_name : {
    library_name : {
        "CMakeLists.txt" : generator.LIB_CMAKE,
        "README.md" : generator.LIB_README,
        "src" : {},
        "include" : {
            "CMakeSharedHeaders.txt" : "",
            library_name : {}
        }
    }
}, lambda library_name : {
    "library" : library_name
})
