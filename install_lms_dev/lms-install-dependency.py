#!/usr/bin/env python3
#Installs a dependency with all its dependencies
import sys, os
from lms import install_utils

if len(sys.argv) != 2:
    print("Usage: lms-flags <dependency>")
    sys.exit(1)

package = sys.argv[1]

def installPackageWithDependencies(package):
    packageUrl = install_utils.getPackageUrlFromName(package)

    #check if a url was set
    if packageUrl == None:
        print("Package not found: "+package)
        sys.exit(1)

    print(packageUrl)

    #install package
    install_utils.installPackage(package,packageUrl)

    #get dependencies
    dependencies = install_utils.getPackageDependencies(package)
    print(dependencies)

    for dependency in dependencies:
        print("installing dependency: " +dependency) 
        installPackageWithDependencies(dependency)

installPackageWithDependencies(package)
