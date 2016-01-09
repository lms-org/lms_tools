#!/usr/bin/env python3
from lms import generator

generator.cli("lms-create-mod", lambda module_name : {
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
}, lambda module_name : {
    "module" : module_name,
    # Generate an uppercase version for header include guards (e.g. TEST_MODULE)
    "module_upper" : module_name.upper(),
    # Generate a camelcase version for the class name (e.g. TestModule)
    "module_camel" : generator.camel_case(module_name)
})
