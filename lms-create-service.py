#!/usr/bin/env python3
import sys
from lms import generator

# Check if the module name was given as command line argument
if len(sys.argv) != 2:
    print("Usage: lms-create-service <module_name>")
    sys.exit(1)

# Service's name (e.g. test_service)
service_name = sys.argv[1]

if service_name == "":
    print("Service name must not be empty")
    sys.exit(1)

if "/" in service_name or "\\" in service_name:
    print("Service name must not contain / or \\")
    sys.exit(1)

try:
    generator.mktree(".", {
        service_name : {
            "CMakeLists.txt" : generator.SERVICE_CMAKE,
            "README.md" : generator.SERVICE_README,
            "src" : {
                service_name + ".cpp" : generator.SERVICE_SOURCE,
                "interface.cpp" : generator.SERVICE_INTERFACE
            },
            "include" : {
                "CMakeSharedHeaders.txt" : "",
                service_name : {
                    service_name + ".h" : generator.SERVICE_HEADER
                }
            }
        }
    }, {
        "service" : service_name,
        # Generate an uppercase version for header include guards (e.g. TEST_SERVICE)
        "service_upper" : service_name.upper(),
        # Generate a camelcase version for the class name (e.g. TestService)
        "service_camel" : generator.camel_case(service_name)
    })

except FileExistsError:
    print("Service creation failed")
    sys.exit(1)
