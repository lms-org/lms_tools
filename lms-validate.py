#!/usr/bin/env python3
import sys
from lms import validation

# Check if a path was given as command line argument
if len(sys.argv) != 2:
    print("Usage: lms-validate <file_or_folder>")
    sys.exit(1)

validation.validate(sys.argv[1])
