#!/usr/bin/env python3
from lms import generator

generator.cli("lms-create-service", lambda service_name : {
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
}, lambda service_name : {
    "service" : service_name,
    # Generate an uppercase version for header include guards (e.g. TEST_SERVICE)
    "service_upper" : service_name.upper(),
    # Generate a camelcase version for the class name (e.g. TestService)
    "service_camel" : generator.camel_case(service_name)
})
