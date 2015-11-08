#!/usr/bin/env python3
import sys, os, re, string

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

# Generate an uppercase version for header include guards (e.g. TEST_MODULE)
module_name_upper = module_name.upper()
# Generate a camelcase version for the class name (e.g. TestModule)
module_name_camel = re.sub(r"(?:^|_)([a-z])", lambda x: x.group(1).upper(),
    module_name)

try:
    os.mkdir(module_name)
    os.mkdir(os.path.join(module_name, "src"))
    os.mkdir(os.path.join(module_name, "include"))
except FileExistsError:
    print("Module directory is already existing: {0}".format(module_name))
    sys.exit(1)

def write_templ_file(file, content):
    with open(os.path.join(module_name, *file), "w") as f:
        f.write(string.Template(content).substitute(module=module_name,
            module_upper=module_name_upper, module_camel=module_name_camel))

write_templ_file(["CMakeLists.txt"],
"""set(SOURCES
    "src/${module}.cpp"
    "src/interface.cpp"
)

set(HEADERS
    "include/${module}.h"
)

include_directories(include)
add_library(${module} MODULE $${SOURCES} $${HEADERS})
target_link_libraries(${module} PRIVATE lmscore)
""")

write_templ_file(["README.md"],
"""# $module

## Data channels

## Config

## Dependencies
""")

write_templ_file(["include", module_name + ".h"],
"""#ifndef ${module_upper}_H
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
""")

write_templ_file(["src", module_name + ".cpp" ],
"""#include "${module}.h"

bool ${module_camel}::initialize() {
    return true;
}

bool ${module_camel}::deinitialize() {
    return true;
}

bool ${module_camel}::cycle() {
    return true;
}
""")

write_templ_file(["src", "interface.cpp"],
"""#include "${module}.h"

extern "C" {
void* getInstance () {
    return new ${module_camel}();
}
}
""")
