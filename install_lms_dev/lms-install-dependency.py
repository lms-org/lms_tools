#!/usr/bin/env python3
import sys, os
from lms import install_utils

if len(sys.argv) != 2:
    print("Usage: lms-flags <dependency>")
    sys.exit(1)

package = sys.argv[1]

packageUrl = install_utils.getPackageUrlFromName(package)

#check if a url was set
if packageUrl == None:
    print("Package not found!")
    sys.exit(1)

print(packageUrl)

install_utils.installPackage(package,packageUrl)
# TODO check if package is valid


