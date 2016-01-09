import os, string, re, sys

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

def cli(tool_name, tree, params):
    # Check if the name was given as command line argument
    if len(sys.argv) != 2:
        print("Usage: {} <name>".format(tool_name))
        sys.exit(1)

    # Object's name (e.g. test_lib, my_module, super_service)
    name = sys.argv[1]

    if name == "" :
        print("Name must not be empty")
        sys.exit(1)

    if "/" in name or "\\" in name:
        print("Name must not contain / or \\")
        sys.exit(1)

    try:
        mktree(".", tree(name), params(name))
    except FileExistsError:
        print("Creation failed")
        sys.exit(1)

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

SERVICE_CMAKE = """set(SOURCES
    "src/${service}.cpp"
    "src/interface.cpp"
)

set(HEADERS
    "include/${service}/${service}.h"
)

include_directories(include)
add_library(${service} SHARED $${SOURCES} $${HEADERS})
target_link_libraries(${service} PRIVATE lmscore)
"""

SERVICE_README = """# $service

## Config

## Dependencies
"""

SERVICE_HEADER = """#ifndef ${service_upper}_H
#define ${service_upper}_H

#include <lms/service.h>

namespace ${service} {

/**
 * @brief LMS service ${service}
 **/
class ${service_camel} : public lms::Service {
public:
    bool init() override;
    void destroy() override;
};

} // namespace ${service}

#endif // ${service_upper}_H
"""

SERVICE_SOURCE = """#include "${service}/${service}.h"

namespace ${service} {

bool ${service_camel}::init() {
    return true;
}

void ${service_camel}::destroy() {
}

} // namespace ${service}
"""

SERVICE_INTERFACE = """#include "${service}/${service}.h"

LMS_SERVICE_INTERFACE(${service}::${service_camel})
"""
