import os, string, re

def mktree(path, tree, params):
    for child, content in tree.items():
        child_path = os.path.join(path, child)

        if isinstance(content, dict):
            os.mkdir(child_path)
            mktree(child_path, content, params)
        else:
            with open(child_path, "w") as f:
                f.write(string.Template(content).substitute(**params))

def camel_case(name):
    return re.sub(r"(?:^|_)([a-z])", lambda x: x.group(1).upper(), name)

LIB_CMAKE = """set(SOURCES
# src/file.cpp
)

set(HEADERS
# include/${library}/file.h
)

include_directories(include)
add_library(${library} SHARED $${SOURCES} $${HEADERS})
target_link_libraries(${library} PRIVATE lmscore)
"""

LIB_README = """# ${library}

## Dependencies
"""

MOD_CMAKE = """set(SOURCES
    "src/${module}.cpp"
    "src/interface.cpp"
)

set(HEADERS
    "include/${module}.h"
)

include_directories(include)
add_library(${module} MODULE $${SOURCES} $${HEADERS})
target_link_libraries(${module} PRIVATE lmscore)
"""

MOD_README = """# $module

## Data channels

## Config

## Dependencies
"""

MOD_HEADER = """#ifndef ${module_upper}_H
#define ${module_upper}_H

#include <lms/datamanager.h>
#include <lms/module.h>

/**
 * @brief LMS module ${module}
 **/
class ${module_camel} : public lms::Module {
public:
    bool initialize() override;
    bool deinitialize() override;
    bool cycle() override;
};

#endif // ${module_upper}_H
"""

MOD_SOURCE = """#include "${module}.h"

bool ${module_camel}::initialize() {
    return true;
}

bool ${module_camel}::deinitialize() {
    return true;
}

bool ${module_camel}::cycle() {
    return true;
}
"""

MOD_INTERFACE = """#include "${module}.h"

LMS_MODULE_INTERFACE(${module_camel})
"""
